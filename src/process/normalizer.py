import pandas as pd


class Normalizer:
    def __init__(self):
        """
        Load the data.
        """
        self.tracks = pd.read_csv('./data/tracks.csv', sep=',')
        self.raw_genres = pd.read_csv('./data/raw_genres.csv', sep=',')

    def replace_genre_ids(self, genre_ids):
        """
        Search raw_genres.csv for the genre.
        params: genres_ids: list of ids
        return: genres: list of genres
        """
        genres = []

        for str_id in genre_ids:
            if str_id == '':
                break
            genre = self.raw_genres.loc[(
                self.raw_genres['genre_id'] == int(str_id)), 'genre_title'].to_string().split(' ')[-1]
            genres.append(genre)

        return genres

    # def remove_duplicates(self):

    # def to_csv(self):

    def get_genre_names(self, row_genres):
        """
        Replace genre_id for the name of the genre.
        params: row_genres: specific row with the 'genres' column only
        return: genres: list of genres
        """
        bad_chars = [' ', '[', ']']

        filter_bad_chars = ''.join(
            (filter(lambda i: i not in bad_chars, row_genres)))
        genre_ids = filter_bad_chars.split(',')

        return self.replace_genre_ids(genre_ids)

    def process_data(self):
        """
        Columns: track title, artist name, release date, genres, all genres
        """

        self.tracks['genres'] = self.tracks.apply(
            lambda row: self.get_genre_names(row['genres']), axis=1)

        self.tracks['genres_all'] = self.tracks.apply(
            lambda row: self.get_genre_names(row['genres_all']), axis=1)

        # tracks_sel_columns = self.tracks[[
        #     'title', 'name (artist)', 'date_released', 'genres', 'genres_all']]
