import csv


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre


class MovieCollection:
    def __init__(self, csv_file):
        self.movies = []
        self.load_movies(csv_file)

    def load_movies(self, csv_file):
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                movie = Movie(row['Title'], int(row['Year']), row['Genre'])
                self.movies.append(movie)

    def get_movies_by_genre(self, genre):
        return [movie for movie in self.movies if movie.genre.lower() == genre.lower()]
