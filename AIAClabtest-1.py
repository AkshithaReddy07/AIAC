def recommend_movies(movies, preferred_genre):
    """
    Recommend movies based on the user's preferred genre.

    Args:
        movies (list of dict): Each dict has 'title' and 'genre' keys.
        preferred_genre (str): The genre to filter movies by.

    Returns:
        list: Titles of movies matching the preferred genre.
    """
    return [movie['title'] for movie in movies if movie['genre'].lower() == preferred_genre.lower()]

# Example usage:
movies = [
    {'title': 'Inception', 'genre': 'Sci-Fi'},
    {'title': 'The Godfather', 'genre': 'Crime'},
    {'title': 'Interstellar', 'genre': 'Sci-Fi'},
    {'title': 'The Dark Knight', 'genre': 'Action'},
]

recommended = recommend_movies(movies, 'Sci-Fi')
print(recommended)  # Output: ['Inception', 'Interstellar']