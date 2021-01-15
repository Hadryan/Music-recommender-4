from neo4j import GraphDatabase
from src.models.person import Person
from src.models.liked import Liked
from src.models.listened import Listened
from ..neo4j.connection_provider import ConnectionProvider
from faker import Faker
from random import randrange, random
from datetime import datetime


class PersonCreator:
    @staticmethod
    def run(quantity=100):
        faker = Faker()
        ConnectionProvider.cleanup_edges(Listened)
        ConnectionProvider.cleanup_edges(Liked)
        ConnectionProvider.cleanup_nodes(Person)
        for _ in range(quantity):
            params = {}
            params['name'] = faker.name()
            params['birth_date'] = datetime(randrange(1950, 2000), randrange(1,12),randrange(1,28)).strftime("%Y")
            person = Person(params)
            ConnectionProvider.create_node(person)
            ConnectionProvider.create_edge_to_random_music(person)
            # print('.')


if __name__ == "__main__":
    PersonCreator.run()
