class Album:
    def __init__(self, album_name: str, number_of_songs: int, album_artist: str):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

    def __repr__(self):
        return self.__str__()


# 3. Create albums1 with 5 Album objects and print
albums1 = [
    Album("Abbey Road", 17, "The Beatles"),
    Album("Thriller", 9, "Michael Jackson"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("Back in Black", 10, "AC/DC"),
    Album("Hotel California", 9, "Eagles")
]
print("Initial albums1:")
print(albums1)

# 4. Sort according to number_of_songs and print
albums1.sort(key=lambda album: album.number_of_songs)
print("\nalbums1 sorted by number of songs:")
print(albums1)

# 5. Swap element at index 0 with element at index 1 and print
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nalbums1 after swapping index 0 and index 1:")
print(albums1)

# 6 & 7. Create albums2 with 5 Album objects and print
albums2 = [
    Album("Born to Run", 8, "Bruce Springsteen"),
    Album("A Night at the Opera", 12, "Queen"),
    Album("Blue", 10, "Joni Mitchell"),
    Album("Purple Rain", 9, "Prince"),
    Album("Bad", 10, "Michael Jackson")
]
print("\nInitial albums2:")
print(albums2)

# 8. Copy all albums from albums1 into albums2
albums2.extend(albums1)

# 9. Add two specific albums to albums2
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

# 10. Sort albums2 alphabetically according to album_name and print
albums2.sort(key=lambda album: album.album_name.lower())
print("\nalbums2 sorted alphabetically by album name:")
print(albums2)

# 11. Search for 'Dark Side of the Moon' in albums2 and print its index
target_name = "Dark Side of the Moon"
found_index = None
for index, album in enumerate(albums2):
    if album.album_name == target_name:
        found_index = index
        break

print(f"\nIndex of '{target_name}' in albums2: {found_index}")