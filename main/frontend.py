import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit, QSplitter, QMainWindow
from backend import MovieCollection


class MovieApp(QMainWindow):
    def __init__(self, movie_collection):
        super().__init__()
        self.movie_collection = movie_collection
        self.initUI()

    def initUI(self):
        # Create a dropdown menu with a list of genres
        self.genreDropdown = QComboBox(self)
        genres = list(
            set([movie.genre for movie in self.movie_collection.movies]))
        genres.sort()
        self.genreDropdown.addItems(genres)

        # Create a list widget to display the movies
        self.movieList = QListWidget(self)

        # Create a text edit widget to show the movie description
        self.movieDescription = QTextEdit(self)
        self.movieDescription.setReadOnly(True)

        # Create a layout and add the widgets to it
        genreLayout = QHBoxLayout()
        genreLayout.addWidget(QLabel('Select a genre:'))
        genreLayout.addWidget(self.genreDropdown)

        movieLayout = QHBoxLayout()
        movieLayout.addWidget(QLabel('Movies:'))
        movieLayout.addWidget(self.movieList)

        descriptionLayout = QHBoxLayout()
        descriptionLayout.addWidget(QLabel('Description:'))
        descriptionLayout.addWidget(self.movieDescription)

        mainLayout = QSplitter()
        mainLayout.addWidget(self.genreDropdown)
        mainLayout.addWidget(self.movieList)
        mainLayout.addWidget(self.movieDescription)

        # Set the layout for the main window
        self.setCentralWidget(mainLayout)

        # Connect the dropdown selection to the updateMovies function
        self.genreDropdown.currentTextChanged.connect(self.updateMovies)

        # Connect the movie selection to the updateDescription function
        self.movieList.itemClicked.connect(self.updateDescription)

    def updateMovies(self, genre):
        # Get the movies based on the selected genre
        moviesToShow = self.movie_collection.get_movies_by_genre(genre)

        # Clear the existing movie list and add the filtered movies to it
        self.movieList.clear()
        for movie in moviesToShow:
            self.movieList.addItem(movie.title)

    def updateDescription(self, item):
        # Get the movie description based on the selected movie title
        movieTitle = item.text()
        movie = next(
            (m for m in self.movie_collection.movies if m.title == movieTitle), None)
        if movie:
            description = f'{movie.title} ({movie.year}) - {movie.genre}\n\n{self.get_movie_description(movie)}'
            self.movieDescription.setPlainText(description)
        else:
            self.movieDescription.setPlainText('')

    def get_movie_description(self, movie):
        # Function to get the movie description (replace with your own implementation)
        # Here we're just using a placeholder string
        return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed efficitur arcu vel turpis vestibulum, eu mollis odio consequat. Nulla eget diam ligula. Sed gravida fringilla nunc, sit amet hendrerit odio posuere eget. Nulla convallis gravida metus, quis rutrum turpis feugiat nec.'


if __name__ == '__main__':
    movie_collection = MovieCollection('main/movies.csv')
    app = QApplication(sys.argv)
    ex = MovieApp(movie_collection)
    ex.show()
    sys.exit(app.exec_())
