from neo4j import GraphDatabase
from src.models.person import Person

class ConnectionProvider:
    __instance = None

    def __init__(self):
        if ConnectionProvider.__instance:
            raise Exception("This class is a singleton!")
        else:
            ConnectionProvider.__instance = self
            self.driver = GraphDatabase.driver('bolt://localhost:11003', auth=('neo4j', '123mudar'))

    @staticmethod
    def getDb():
        return ConnectionProvider.getInstance().driver.session(database='musicrecommender')

    @staticmethod
    def getInstance():
        if not ConnectionProvider.__instance:
            ConnectionProvider()
        return ConnectionProvider.__instance


    @staticmethod
    def create_node(klass):
        cypher = f'CREATE (n:{type(klass).__name__} {klass.params_str()})'
        ConnectionProvider.getDb().run(cypher)


if __name__ == "__main__":
    person = Person({'name': 'Eduardo', 'birth_date': '25/12/1997'})
    ConnectionProvider.create_node(person)
