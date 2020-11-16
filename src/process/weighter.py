from src.models.music import Music

class Weighter:
    def __init__(self, musics):
        self.musics = musics

    @staticmethod
    def to(musics):
        return Weighter(musics).__calculate()

    def __calculate(self):
        similarities = self.__get_similarities()
        totals = []
        totals.append(similarities['genres'] * 0.80)
        totals.append(similarities['release_date'] * 0.20)
        return sum(totals)

    def __get_similarities(self):
        return {
            'genres': self.__genres_similarity(),
            'release_date': self.__release_date_similarity()
        }

    def __genres_similarity(self):
        [genres1, genres2] = sorted(map(lambda m: m.genres, self.musics), key=len)
        same = [g for g in genres1 if g in genres2]
        # percentage of how many are equals based on len of the bigger
        return (len(same) * (len(genres1)/len(genres2)))/len(genres2)

    def __release_date_similarity(self):
        [date1, date2] = map(lambda m: m.release_date, self.musics)
        diff = abs(date1 - date2)
        return max(0, 1-(diff/10))
