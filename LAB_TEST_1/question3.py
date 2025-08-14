# Movie recommendation system based on user's preferred genre

def recommend_movies(movies, genre):
    """
    Returns a list of movie titles matching the given genre (case-insensitive).
    """
    genre = genre.lower()
    return [movie['title'] for movie in movies if movie['genre'].lower() == genre]

# Few shot prompting examples:
movies = [
    {'title': 'gita govindam', 'genre': 'romance'},
    {'title': 'Srinivasa kalyanam', 'genre': 'family'},
    {'title': 'shathamanambavathi', 'genre': 'family'},
    {'title': 'anabelle', 'genre': 'horror'}
]

# Example usages:
print("Few shot prompting examples:")
print("recommend_movies(movies, 'horror') ->", recommend_movies(movies, 'horror'))
print("recommend_movies(movies, 'Romance') ->", recommend_movies(movies, 'Romance'))
print("recommend_movies(movies, 'family') ->", recommend_movies(movies, 'family'))

# User input option
user_genre = input("\nEnter your preferred genre: ")
recommended = recommend_movies(movies, user_genre)
if recommended:
    print("Recommended movies:", recommended)
else:
    print("No movies found for the given genre.")
