class Music:
    def __init__(self, params):
        self.name = params.get('track_name')
        self.artist = params.get('artist_name')
        self.release_date = params.get('release_date')
        self.genres = params.get('genres') or []

    def params_str(self):
        return "{{name: \"{}\", artist: \"{}\", release_date: \"{}\", genres: {}}}".format(self.name, self.artist, self.release_date, self.genres)
