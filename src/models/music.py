class Music:
    def __init__(self, params):
        self.name = params.get('name')
        self.artist = params.get('artist')
        self.release_date = params.get('release_date')
        self.genres = params.get('genres') or []

    @staticmethod
    def get_from_csv_row(csv_row):
        params = {}
        params['name'] = csv_row['name']
        params['artist'] = csv_row['artist']
        params['release_date'] = csv_row['release_date']
        genres = csv_row['genres'][1:len(csv_row['genres'])-1]
        params['genres'] = genres.replace('\'', '').split(',')
        return Music(params)

    def params_str(self):
        return "{{name: \"{}\", artist: \"{}\", release_date: \"{}\", genres: {}}}".format(self.name, self.artist, self.release_date, self.genres)
