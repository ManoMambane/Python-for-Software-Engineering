# Define list of top 5 favorite movies
movies = [
    "Inception",
    "The Matrix",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction"
]

# Print using enumerate() starting at index 1
for index, movie in enumerate(movies, start=1):
    print(f"Movie {index}: {movie}")