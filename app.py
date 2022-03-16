from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    #movies = movie_repository_singleton.get_all_movies()
    movies = {Movie("Spongebob", "Me",5),
        Movie( "idk", "steve", 1)}

    return render_template('list_all_movies.html', list_movies_active=True, movie=movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    movie_title=request.form.get("movie-title")
    director_name=request.form.get("directorName")
    movie_rating= int(request.form.get("ratings"))
    movie_repository_singleton.create_movie(movie_title,director_name,movie_rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    movie_title = request.args.get('title')
    found_movie = movie_repository_singleton.get_movie_by_title(self, movie_title)
    if (found_movie = None):
        rating_statement = "Movie not found. Try another title."
    else: 
        rating_statement = "Movie " + found_movie.title + " found with a rating of " + found_movie.rating + ", by " + found_movie.director + "."
    return render_template('search_movies.html', search_active=True, ratinginput=rating_statement)
