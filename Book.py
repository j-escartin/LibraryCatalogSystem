class Book: # Declare the Class Book

  def __init__(self, title, author, availability = True): # Initialize the init constructor
    self.title = title
    self.author = author
    self.availability = availability
  
  # To Display the book Info
  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print("Availability: Available" if self.availability else "Availability: Not Available")
    print()

  # This one for checking out
  def check_out(self):
    if self.availability:
      print(f"You have checkout the book entitled: {self.title}")
      self.availability = False
    else:
      print(f"Sorry the book entitled: {self.title} is not available")

  # This one is for cheking in
  def check_in(self):
    print(f"Thank you for returning the book entitled: {self.title}")
    self.availability = True