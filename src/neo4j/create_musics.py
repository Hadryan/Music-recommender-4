from neo4j import GraphDatabase
from src.models.music import Music
from ..neo4j.connection_provider import ConnectionProvider
import pandas as pd


class MusicCreator:
    @staticmethod
    def run():
        ConnectionProvider.cleanup_nodes(Music)
        tracks = pd.read_csv('./data/sampled_tracks.csv', sep=',')
        for track in tracks.iterrows():
            params = {}
            params['name'] = track[1]['track_name']
            params['artist'] = track[1]['artist_name']
            params['release_date'] = track[1]['release_date']
            genres = track[1]['genres'][1:len(track[1]['genres'])-1]
            params['genres'] = genres.replace('\'', '').split(',')
            music = Music(params)
            ConnectionProvider.create_node(music)
            print('.')


if __name__ == "__main__":
    MusicCreator.run()
