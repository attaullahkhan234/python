# My Library Book Organiser

books = ["Harry Potter", "The Hobbit", "Matilda", "The Alchemist", "Atomic Habits"]

print("Book list:", books)

print("Total books:", len(books))
print("First book:", books[0])
print("Last book:", books[-1])
print("First three books:", books[:3])

books.append("The Little Prince")
print("\nAfter adding The Little Prince:", books)

books.remove("Matilda")
print("After removing Matilda:", books)

books.sort()
print("Sorted book list:", books)

books.reverse()
print("Reversed book list:", books)

librarian = {
    "name": "Mr. Sharma",
    "Library": "School Library",
    "Experience": 5
}

print("\nLibrarian profile:", librarian)

print("Name:", librarian["name"])
print("Experience:", librarian.get("Experience", "not found"))

librarian["Experience"] = 6
librarian["Email"] = "mr.sharma@school.com"

librarian.pop("Library")

print("Updated librarian profile:", librarian)


book_ids = [101, 102, 103, 104, 105]

book_names = [
    "Harry Potter",
    "The Hobbit",
    "The Alchemist",
    "Atomic Habits",
    "The Little Prince"
]

book_directory = dict(zip(book_ids, book_names))

print("\nBook directory:", book_directory)

print("Book with ID 103:", book_directory[103])