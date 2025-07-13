from datetime import datetime

class Movie:
    def __init__(self, name):
        self.name = name
        self.date_added = datetime.now()
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0.0
