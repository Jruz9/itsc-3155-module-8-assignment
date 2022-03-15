from src.repositories.movie_repository import movie_repository_singleton


def test_get_all_movies():
    movie_repository_singleton.create_movie("Cloverfield", "Mark Cuban",5)
    movie_repository_singleton.create_movie( "Role Models", "Jonah Hill", 4)
    movieList = movie_repository_singleton.get_all_movies()
    assert "Me" == movieList[0].director, "test passed"
    assert "Spongebob" == movieList[0].title, "test passed"
