from src.models.music import Music
from src.neo4j.connection_provider import ConnectionProvider
import numpy as np
from time import time
import random

class Popularity:
    def __init__(self, user_id, music_ids):
        self.music_ids = music_ids
        self.user_id = user_id

    # @staticmethod
    def to(user_id, music_ids):
        return Popularity(user_id, music_ids).__calculate()

    def __calculate(self):
        musics_listened_popularity = ConnectionProvider.get_musics_listened_popularity(self.user_id)
        musics_popularity = ConnectionProvider.get_musics_popularity(self.music_ids)
        # mean of returned musics (for a specific user)
        self.mean = np.mean(musics_listened_popularity)
        self.std = np.std(musics_listened_popularity)
        self.max = abs(self.__zscore(0 if self.mean > 0.5 else 1))
        # print(musics_listened_popularity, musics_popularity)        
        # print(self.mean, self.std)
        results = [self.__zscore(music) for music in musics_popularity]
        return list(map(self.__normalize, results))

    def __zscore(self, value):
        return (value - self.mean) / self.std

    def __normalize(self, value):
        return 1 - (abs(value) / self.max)  


# if __name__ == "__main__":
#     random.seed(time())
#     music_ids = [21]
#     print(Popularity.to('117', [str(id) for id in music_ids]))
