from neo4j import GraphDatabase
from src.models.music import Music
from src.models.similarity import Similarity
from src.process.weighter import Weighter
from ..neo4j.connection_provider import ConnectionProvider
from pandas import read_csv


class EdgeCreator:
    @staticmethod
    def run():
        EdgeCreator.music_music()

    @staticmethod
    def music_music():
        ConnectionProvider.cleanup_edges(Similarity)
        tracks = read_csv('./data/sampled_tracks.csv', sep=',')
        musics = []
        for track in tracks.iterrows():
            musics.append(Music.get_from_csv_row(track[1]))
        i = 0
        for music in musics[0:len(musics) - 2]:
            for j in range(i, len(musics) - 1):
                weight = Weighter.to([music, musics[j+1]])
                similarity = Similarity(weight)
                ConnectionProvider.create_edge(music, musics[j+1], similarity)
                print('.')
            i+=1


if __name__ == "__main__":
    EdgeCreator.run()
