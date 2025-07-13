import unittest
from movie import Movie
from movie_service import MovieService

class TestMovieService(unittest.TestCase):
    def test_add_and_retrieve_movie(self):
        service = MovieService()
        service.add_movie("Koto Aiye")
        self.assertIsNotNone(service.get_movie("Koto Aiye"))

    def test_rate_movie(self):
        service = MovieService()
        service.add_movie("Titanic")
        service.rate_movie("Titanic", 5)
        self.assertEqual(service.get_movie("Titanic").get_average_rating(), 5.0)

    def test_multiple_ratings(self):
        service = MovieService()
        service.add_movie("Ipadabo Abija")
        service.rate_movie("Ipadapo Abija", 4)
        service.rate_movie("Ipadabo Abija", 2)
        self.assertEqual(service.get_movie("Ipadabo Abija").get_average_rating(), 2.0)

if __name__ == '__main__':
    unittest.main()
