from Book import Book
from Library import Library

def main():

  # Adding books
  book_1 = Book("Clean Code", "Robert Cecil Martin")
  book_2 = Book("The Pragmatic Programmer", "Dave Thomas")
  book_3 = Book("The Clean Coder", "Robert Cecil Martin")

  # Initialize Library
  library = Library()

  # Add the books to the library
  library.add_book(book_1)
  library.add_book(book_2)
  library.add_book(book_3)
  
  # Double checkout
  book_1.check_out()
  book_1.check_out()

  # Checkin
  book_1.check_in()

  # Search By Title
  library.search_by_title("The Pragmatic Programmer")

  # Search By Author
  library.search_by_author("Robert Cecil Martin")

  #See all the library cards catalog
  library.display_catalog()

if __name__ == "__main__":
  main()