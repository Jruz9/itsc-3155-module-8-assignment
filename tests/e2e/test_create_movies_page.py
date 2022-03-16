from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie_page():

    movie_repository_singleton.create_movie("Narnia","Michael Apted","3")
    movies=movie_repository_singleton.get_all_movies()

    assert "Narnia"== movies[0].title
