from movie import Movie


class MovieService:
    def __init__(self):
        self.movies = {}

    def add_movie(self, name):
        self.movies[name.lower()] = Movie(name)

    def rate_movie(self, name, rating):
        movie = self.movies.get(name.lower())
        if movie:
            movie.add_rating(rating)

    def get_movie(self, name):
        return self.movies.get(name.lower())

    def get_all_movies(self):
        return self.movies.values()
