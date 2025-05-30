from neo4j import GraphDatabase
import stanza

# Initialize NLP pipeline
nlp = stanza.Pipeline('en', processors='tokenize,pos,lemma,depparse', use_gpu=False)

class NLPNeo4jImporter:
    def __init__(self, neo4j_uri="bolt://localhost:7687", user="neo4j", password="password", db="dictionary"):
        self.driver = GraphDatabase.driver(neo4j_uri, auth=(user, password))
        self.db = db

    def close(self):
        self.driver.close()

    def store_sentence(self, text: str):
        doc = nlp(text)
        with self.driver.session(database=self.db) as session:
            for i, sent in enumerate(doc.sentences):
                sent_id = f"{hash(text)}_{i}"
                session.write_transaction(self._create_sentence_graph, sent_id, sent)

    @staticmethod
    def _create_sentence_graph(tx, sent_id: str, sent):
        # Create sentence node
        tx.run("MERGE (s:Sentence {id: $id})", id=sent_id)

        # Create word nodes and relationships
        for word in sent.words:
            tx.run("""
                MERGE (w:Word {id: $wid})
                SET w.text = $text, w.lemma = $lemma, w.pos = $pos
                MERGE (s:Sentence {id: $sid})
                MERGE (s)-[:CONTAINS]->(w)
            """, wid=f"{sent_id}_{word.id}", text=word.text, lemma=word.lemma, pos=word.upos, sid=sent_id)

        # Add dependency relationships
        for word in sent.words:
            if word.head != 0:
                tx.run("""
                    MATCH (from:Word {id: $from_id})
                    MATCH (to:Word {id: $to_id})
                    MERGE (from)-[r:DEPENDS_ON {type: $rel}]->(to)
                """, from_id=f"{sent_id}_{word.id}",
                     to_id=f"{sent_id}_{word.head}",
                     rel=word.deprel)

# Example usage
if __name__ == "__main__":
    text = "The dog was barking loudly."
    importer = NLPNeo4jImporter(password="test1234")
    try:
        importer.store_sentence(text)
        print("Sentence stored in Neo4j.")
    finally:
        importer.close()
