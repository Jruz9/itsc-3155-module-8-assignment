from src.repositories.movie_repository import movie_repository_singleton

def test_get_movie_by_title():
    movie_repository_singleton.create_movie("The Fast and the Furious", "Rob Cohen",7)
    movie_repository_singleton.create_movie("2 Fast 2 Furious", "John Singleton",2)
    movie_repository_singleton.create_movie("Tokyo Drift", "Justin Lin",8)
    movie_repository_singleton.create_movie("Fast & Furious 4", "Justin Lin",6)
    movie_repository_singleton.create_movie("Fast 5", "Justin Lin",6)
    movie_repository_singleton.create_movie("Fast & Furious 6", "Justin Lin",7)
    movie_repository_singleton.create_movie("Fast & Furious 7", "James Wan",4)
    movie_repository_singleton.create_movie("The Fate of the Furious", "F. Gary Gray",7)
    movie_repository_singleton.create_movie("F9", "Justin Lin",6)
    assert "Tokyo Drift" == movie_repository_singleton.get_movie_by_title(self, "Tokyo Drift").title
    assert None == movie_repository_singleton.get_movie_by_title(self, "Fast & Furious 10").title