from flask.testing import FlaskClient
from app import search_movies
def test_search_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response_data