from neo4j import GraphDatabase
from src.models.music import Music
from src.models.similarity import Similarity
from ..neo4j.connection_provider import ConnectionProvider
import pandas as pd


class MusicCreator:
    @staticmethod
    def run():
        ConnectionProvider.cleanup_edges(Similarity)
        ConnectionProvider.cleanup_nodes(Music)
        tracks = pd.read_csv('./data/sampled_tracks.csv', sep=',')
        for track in tracks.iterrows():
            music = Music.get_from_csv_row(track[1])
            ConnectionProvider.create_node(music)
            print('.')


if __name__ == "__main__":
    MusicCreator.run()
