from neo4j import GraphDatabase
from .neo4j.connection_provider import ConnectionProvider
from .process.popularity import Popularity

class Recommender:
    """
    @params
    user_id: the Id of the user.
    n_recomm: number of tracks that shall be recommended to the specified user.
    """
    def __init__(self, user_id, n_recomm):
        self.user_id = user_id
        self.n_recomm = n_recomm

    def strange_behavior(self, obj):
        ids = []
        coefs = []
        tracks = []
        for o in obj:
            ids.append(o[0])
            coefs.append(o[4])
            tracks.append([o[1], o[2]])
        return (ids, coefs, tracks)

    def takeThird(self, elem):
        """
        Used for sorting the list.
        """
        return elem[2]        
    
    def recommend_for(self):
        """
        @return
        recomm: array containing the recommended tracks. Each element of the array
        has the following data: [track name, artist name, coefficient of acceptance]
        """
        # fetch the most listened track for provided user_id
        most_listened = self.query_most_listened().value()
        # fetch all tracks + similarity coefficient to the track 'most_listened'
        tracks = self.query_music(most_listened[0])
        (ids, coefs, tracks_info) = self.strange_behavior(tracks)
        popularity_coefs = Popularity.to(str(self.user_id), ids)
        # calculate the new coefficient with popularity and similarity coefficient
        recomm = [(coef * 0.7) + (pop_coef * 0.3) for coef, pop_coef in zip(coefs, popularity_coefs)]
        for i in range (self.n_recomm):
            tracks_info[i].append(recomm[i])
        tracks_info.sort(key=self.takeThird, reverse=True)
        return tracks_info

    def query_music(self, music_id):
        """
        @params
        music_id: if of the most listened music by a specific user.
        self.n_recomm = number of tracks that will be returned
        @return
        tracks: all tracks and its similarity coefficient (related to the input music_id)
        """
        query = f'MATCH (m1: Music)-[r:Similarity]- (m2: Music) where id(m1)={music_id} return id(m2), m2.name, m2.artist, m2.popularity, r.weight order by r.weight desc limit {self.n_recomm}'
        tracks = ConnectionProvider.getDb().run(query)
        return tracks

    def query_most_listened(self):
        """
        @params
        user_id: the id of the user
        @return
        track: most listened track for the input user_id
        """
        query = f'MATCH (p: Person)-[r:Listened]- (m: Music) where id(p)={self.user_id} return id(m) order by r.times desc limit 1'
        track = ConnectionProvider.getDb().run(query)
        return track
