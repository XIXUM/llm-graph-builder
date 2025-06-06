from neo4j import GraphDatabase, basic_auth
from typing import List, Dict, Any

class Neo4jDefaultClient:
    def __init__(self, uri: str = "bolt://localhost:7687", user: str = "neo4j", password: str = "password",
                 database: str = "dictionary"):
        self.uri = uri
        self.user = user
        self.password = password
        self.database = "neo4j"
        self.driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    def close(self):
        if self.driver:
            self.driver.close()

    def run_query(self, cypher_query: str, parameters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Execute a Cypher query and return the result as a list of dictionaries.
        """
        parameters = parameters or {}
        with self.driver.session(database=self.database) as session:
            result = session.run(cypher_query, parameters)
            return [record.data() for record in result]


class Neo4jDatabaseClient(Neo4jDefaultClient):
    def __init__(self, uri: str = "bolt://localhost:7687", user: str = "neo4j", password: str = "password",
                 database: str = "neo4j"):
        super().__init__(uri, user, password)
        self.database = database



####
# enable to test it headless.
# Example usage:
if __name__ == "__main__":
    client = Neo4jDatabaseClient(password="test1234")

    try:
        # Example query
        query = "MATCH (n) RETURN n LIMIT 5"
        results = client.run_query(query)
        for record in results:
            print(record)
    finally:
        client.close()
