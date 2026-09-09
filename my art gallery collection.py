class ArtGallery:

    def __init__(self, gallery_name, owner):
        self.gallery_name = gallery_name
        self.owner = owner
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print("Artwork added:", artwork)

    def show_artworks(self):
        print("\n=== Art Gallery Collection ===")

        if len(self.artworks) == 0:
            print("No artworks in the gallery.")
        else:
            for artwork in self.artworks:
                print("-", artwork)

    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print("Artwork removed:", artwork)
        else:
            print("Artwork not found.")

    def __del__(self):
        print("\nArt Gallery object is closed/deleted.")


gallery = ArtGallery("Khan Art Gallery", "Khan")

while True:

    print("\n=== Art Gallery Collection Manager ===")
    print("1. Add Artwork")
    print("2. Show Artworks")
    print("3. Remove Artwork")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        artwork = input("Enter artwork name: ")
        gallery.add_artwork(artwork)

    elif choice == "2":
        gallery.show_artworks()

    elif choice == "3":
        artwork = input("Enter artwork to remove: ")
        gallery.remove_artwork(artwork)

    elif choice == "4":
        print("Exiting Art Gallery...")
        break

    else:
        print("Invalid choice. Try again.")