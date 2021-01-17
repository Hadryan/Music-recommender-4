"""
Usage:
music.py <user_id> <num_of_recomm>
music.py populate
music.py cleanup
"""

from docopt import docopt
from src.recommender import Recommender
import tableprint as tp
from src.neo4j.create_musics import MusicCreator
from src.neo4j.create_persons import PersonCreator
from src.neo4j.create_edges import EdgeCreator
from src.neo4j.connection_provider import ConnectionProvider


def recommend(user_id, num_of_recs):
    """
    This function computes the music recommendation.
    Calls function :py:func:`src.recommender.Recommender.recommend_for`.
    """
    recomm = Recommender(user_id, num_of_recs)
    return recomm


def display(recomm):
    """
    This function displays the recommended tracks.
    @params
    recomm: recommended tracks composed by name of track and artist,
    and coefficient of acceptance.
    """
    headers = ['Track', 'Artist', '[Similarity + Popularity] Coefficient']
    tp.table(recomm, headers)

def populate_database():
    MusicCreator.run()
    PersonCreator.run()
    EdgeCreator.run()

def clean_database():
    ConnectionProvider.cleanup()

def main():
    """
    This function parses the arguments and calls :py:func:`recommend` to get the track
    recommendations, then calls :py:func:`display` to display the recommendations.
    """
    args = docopt(__doc__)
    if (args['populate'] == True):
        populate_database()
    elif (args['cleanup'] == True):
        clean_database()
    else:
        try:
            recomm = Recommender(int(args['<user_id>']), int(args['<num_of_recomm>'])).recommend_for()
            display(recomm)
        except ValueError as ex:
            print("Invalid command: <user_id> and <num_of_recomm> are integers.")


if __name__ == '__main__':
    main()
