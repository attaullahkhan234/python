class playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' '{self.genre}' is ready.")

    def add_song(self, song):
        self.songs.append(song)
        print(f"Song '{song}' added to playlist '{self.name}'.")

    def remove_song(self, song):
            if song in self.songs:
                self.songs.remove(song)
                print(f"'{song}' removed.")
            else:
                print(f"'{song}' not found in the playlist.") 

    def display_songs(self):
        print(f"\n--- {self.name}  ({self.genre}) ---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"- {i}. {song}")
        else:
            print(" No songs yet. Add some!")

    def __del__(self):
        print(f"Playlist '{self.name}' deleted.")

my_playlist = playlist("My Playlist", "Pop")

while True:
    print("\nOptions:")
    print("1. Add a song")
    print("2. Remove a song")
    print("3. Display songs")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        song_name = input("Enter the name of the song to add: ")
        my_playlist.add_song(song_name)
    elif choice == "2":
        song_name = input("Enter the name of the song to remove: ")
        my_playlist.remove_song(song_name)
    elif choice == "3":
        my_playlist.display_songs()
    elif choice == "4":
        print("Exiting the playlist manager.")
        break
    else:
        print("Invalid choice. Please try again.")

        