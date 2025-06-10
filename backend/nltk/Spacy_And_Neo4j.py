import spacy
from neo4j import GraphDatabase

nlp = spacy.load("en_core_web_sm")

text = """
Apple Inc. was founded by Steve Jobs in 1976. The company is based in Cupertino, California.
Tim Cook became CEO in 2011. Apple is known for products like the iPhone and MacBook.
"""

def create_knowledge_graph(tx, entities, relationships):
    # Create entities (nodes)
    for entity, label in entities:
        tx.run("MERGE (e:Entity {name: $name, type: $type})", name=entity, type=label)

    # Create relationships
    for rel in relationships:
        tx.run("""
            MATCH (a:Entity {name: $ent1}), (b:Entity {name: $ent2})
            MERGE (a)-[r:RELATION {type: $rel_type}]->(b)
        """, ent1=rel[0], ent2=rel[1], rel_type=rel[2])

def extract_entities(unstructured_text):
    # Extract entities and relationships
    doc = nlp(unstructured_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    relationships = []

    # Define co-occurrence window (e.g., 14 words)
    window_size = 14
    for sent in doc.sents:
        tokens = [token.text for token in sent]
        for i, ent1 in enumerate(sent.ents):
            for j, ent2 in enumerate(sent.ents):
                if i != j and abs(ent1.start - ent2.start) <= window_size:
                    relationships.append((ent1.text, ent2.text, "CO_OCCURS_WITH"))

    print("Entities:", entities)
    print("Relationships:", relationships)

    return entities, relationships

if __name__ == "__main__":

    entities, relationships = extract_entities(text)

    # Neo4j connection settings
    URI = "bolt://localhost:7687"
    USER = "neo4j"
    PASSWORD = "test1234"

    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

    with driver.session() as session:
        session.execute_write(create_knowledge_graph, entities, relationships)
    driver.close()
