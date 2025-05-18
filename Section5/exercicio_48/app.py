books = {
    "Frankenstein": {
        "author": "Mary Shelley",
        "year": 1818,
        "genre": "Horror"
    },
    "Atlas Shrugged": {
        "author": "Ayn Rand",
        "year": 1957,
        "genre": "Philosophical fiction"
    },
    "The Bitcoin Standard": {
        "author": "Saifedean Ammous",
        "year": 2018,
        "genre": "Economics"
    },
}

print("The books are: %s" % books)

for book in books:
    print("The book %s was written by %s in %d and is a %s book." % (book, books[book]["author"], books[book]["year"], books[book]["genre"]))