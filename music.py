"""
Usage:
music.py <user_id> <num_of_recomm>
"""

from docopt import docopt
from src.recommender import Recommender


def recommend(user_id, num_of_recs):
    """
    This method computes the music recommendation.
    Calls function :py:func:`src.recommender.Recommender.recommend_for`
    """
    Recommender.recommender_for(user_id, num_of_recs)


def main():
    """
    Parse arguments for :py:func:`recommend`
    """
    args = docopt(__doc__)
    try:
        recommend(int(args['<user_id>']), int(args['<num_of_recomm>']))
    except ValueError as ex:
        print("Invalid command: <user_id> and <num_of_recomm> are integers.")


if __name__ == '__main__':
    main()
