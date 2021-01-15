from neo4j import GraphDatabase
from .neo4j.connection_provider import ConnectionProvider


class Recommender:
    """
    @params
    user_id: the Id of the user.
    n_recomm: number of tracks that shall be recommended to the specified user.
    """
    def __init__(self, user_id, n_recomm):
        self.user_id = user_id
        self.n_recomm = n_recomm
    
    @staticmethod
    def recommend_for(self):
        query_music()
        return recomm

    @staticmethod
    def query_music():
        query = f'MATCH (m1: Music)-[r:Similarity]- (m2: Music) where id(m1)=15 return m1, m2 order by r.weight desc limit 1'
        ConnectionProvider.getDb().run(query)
