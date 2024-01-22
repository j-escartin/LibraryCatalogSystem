class Library:
  def __init__(self):
    self.books = [] # Initialize Books

  # Add Books
  def add_book(self, book):
    print(f"You have successfully added the book entitle {book.title} to the library catalog")
    self.books.append(book)

  # Search By Title
  def search_by_title(self, title):
    matching_books = [book.title for book in self.books if book.title.lower() == title.lower()]
    return print(matching_books)
  
  # Search by Author
  def search_by_author(self, author):
    matching_books = [book.title for book in self.books if book.author.lower() == author.lower()]
    return print(matching_books)
  
  # Display all Catalogs
  def display_catalog(self):
    print("Displaying all cards in the catalog")
    for book in self.books:
      book.display_info()