from neo4j import GraphDatabase
from src.models.person import Person
from ..neo4j.connection_provider import ConnectionProvider
from faker import Faker
from random import randrange
from datetime import datetime


class PersonCreator:
    @staticmethod
    def run(quantity=100):
        faker = Faker()
        ConnectionProvider.cleanup_nodes(Person)
        for _ in range(quantity):
            params = {}
            params['name'] = faker.name()
            params['birth_date'] = datetime(randrange(1950, 2000), randrange(1,12),randrange(1,28)).strftime("%Y")
            person = Person(params)
            ConnectionProvider.create_node(person)
            print('.')


if __name__ == "__main__":
    PersonCreator.run()
