# from flask import render_template
from flask import render_template
from app import app
from .request import get_movies

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # message = "Hello World"
    # Getting popular Movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    # print(popular_movies)
    title = 'Home - Welcome to the best Movie Review website online'
    return render_template("index.html",title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    view movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id=movie_id)