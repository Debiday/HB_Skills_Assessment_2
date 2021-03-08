"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   -Encapsulation: Where data lives near the function or code, and
                   reduces errors/ improves speed.
   -Abstraction: Where it is easy to make new items and hiding verbose
                 or complex implementation. e.g. binary
   -Polymorphism: Where it is easy to apply properties of one item to
                  another, creating similar items/classes.

2. What is a class?

A class allows you to make new objects, and creates templates for these
objects to be made. 


3. What is a method?

A method is a function specific to different data types. e.g. lists can `.append`
In classes it is a function defined on a class.


4. What is an instance in object orientation?

An individual occurence of a class. 


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is a template that can be reused by instances of the
class whereas instance attributes only apply to the particular instance and takes
precendence over the class attributes.

e.g. Class attribute: Animals
Instance: Fido
"""


"""2. Road Class"""

class Road : 
    num_lanes = 2
    speed_limit = 25

road_1 = Road() #update road_1 attributes with new values
road_1.num_lanes = 4
road_1.speed_limit = 60

road_2 = Road()


"""3. Update Password"""


class User :
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password
    
    def update_password(self, current, new):
        """Check if current password is correct, 
           update new password"""

        if self.password == current:
            self.password = new
        else:
            print('Invalid password')

"""4. Build a Library"""


class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author

class Library(object):
    """A library object"""

    def __init__(self, name):
        """Create a library with a list of books"""
        self.name = name
        self.books = []
    
    def create_and_add_book(self, book):
        """Instantiate Book object and add it to Library book list"""

        self.books.append(book)

    def find_books_by_author(self, author):
        """Takes in author name and returns author's books"""
        # author = input("Please enter name of Author  >")
        
        list_books = []
        
        for book in self.books: #for all the books in the library
            if author == book.author: #if author matches, append to list
                list_books.append(book.title)
        return list_books


# Example:
# book1 = Book("t", "a") -creating book
# book2 = Book("r", "a")
# book3 = Book("s", "a")
# book4 = Book("q", "b")
# lib1 = Library("lib1") -creating library
# lib1.create_and_add_book(book1) -adding book to library 4 times
# lib1.find_books_by_author("a") #['t', 'r', 's']



"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width

class Square(Rectangle):
    """A square."""

    def __init__(self, length):
        super().__init__(length, length)

    def calculate_area(self, length, width): #check if sides are indeed equal?
        if length == width:
            area = super().calculate_area() #call method from rectangle class
        else:
            print("Invalid square")
            return None
        return area

# Example:
# square1 = Square(10)
# square1.calculate_area()
# extra validation: square1.calculate_area(width, height)

