from neo4j import GraphDatabase
from src.models.person import Person
from src.models.listened import Listened
from random import randrange, random

class ConnectionProvider:
    __instance = None
    __session = None

    def __init__(self):
        if ConnectionProvider.__instance:
            raise Exception("This class is a singleton!")
        else:
            ConnectionProvider.__instance = self
            self.driver = GraphDatabase.driver('bolt://localhost:11003', auth=('neo4j', '123mudar'))
            ConnectionProvider.__session = self.driver.session(database='musicrecommender')

    @staticmethod
    def getDb():
        if not ConnectionProvider.__session:
            ConnectionProvider()
        return ConnectionProvider.__session

    @staticmethod
    def getInstance():
        if not ConnectionProvider.__instance:
            ConnectionProvider()
        return ConnectionProvider.__instance

    @staticmethod
    def create_node(klass):
        cypher = f'CREATE (n:{type(klass).__name__} {klass.params_str()})'
        ConnectionProvider.getDb().run(cypher)

    @staticmethod
    def create_edge(origin, destiny, edge):
        cypher = f'MATCH (origin: {type(origin).__name__} {origin.params_str()}), (destiny: {type(destiny).__name__} {destiny.params_str()})\n'
        cypher += f'CREATE (origin)-[r: {type(edge).__name__} {edge.params_str()}]->(destiny)'
        ConnectionProvider.getDb().run(cypher)

    @staticmethod
    def create_edge_to_random_music(person):
        r = random()
        if(r > 0.7):
            music_id = randrange(1, 99)
            cypher = f'MATCH (origin: Person {person.params_str()}), (destiny: Music) where id(destiny)={music_id}\n'
            cypher += f'CREATE (origin)-[r: Liked]->(destiny)'
            ConnectionProvider.getDb().run(cypher)
            cypher = f'MATCH (origin: Person {person.params_str()}), (destiny: Music) where id(destiny)={music_id}\n'
            cypher += f'CREATE (origin)-[r: Listened {Listened(randrange(5, 10)).params_str()}]->(destiny)'
            ConnectionProvider.getDb().run(cypher)

        for _ in range(randrange(1, 10)):
            music_id = randrange(1, 99)
            cypher = f'MATCH (origin: Person {person.params_str()}), (destiny: Music) where id(destiny)={music_id}\n'
            cypher += f'CREATE (origin)-[r: Listened {Listened(randrange(1, 5)).params_str()}]->(destiny)'
            ConnectionProvider.getDb().run(cypher)

    @staticmethod
    def cleanup_nodes(klass):
        print()
        cypher = f'MATCH (n:{klass.__name__}) DELETE n'
        ConnectionProvider.getDb().run(cypher)

    @staticmethod
    def cleanup_edges(klass):
        cypher = f'MATCH ()-[r:{klass.__name__}]->() DELETE r'
        ConnectionProvider.getDb().run(cypher)

    @staticmethod
    def cleanup():
        cypher = f'MATCH (n) DETACH DELETE n'
        ConnectionProvider.getDb().run(cypher)
