#FLOW:  Functions to be made for library management system using SQLAlchemy:
# add_category() --> add books category
# add_book() --> add new Book
# borrow_book() --> borrow a Book
# update_borrow() --> update borrow date
# search_by_date() --> find borrowed books by date
# category_report() --> count borrowed books by date
# set_limit() --> set monthly borrow limit
# limit_alert() --> check if limit exceeded

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


#database connection
engine = create_engine("sqlite:///libtrack.db")
Base=declarative_base()
Session=sessionmaker(bind=engine)
session=Session()      #all these for insertion and retrieval of data from database

class Category(Base):  #Base is the base class for all our ORM models. It provides the necessary functionality to define tables and map them to Python classes. By inheriting from Base, our Category class becomes an ORM model that can be used to interact with the database.
    __tablename__ = "categories"  #__tablename__ is a special attribute that specifies the name of the table in the database that this class will be mapped to. 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books=relationship("Book", back_populates="category") #relationship to link with Book table backpopulate is used for bidirectional relationship
    
class Book(Base): #to store book details     
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id")) #foreign key to link with Category table
    category = relationship("Category", back_populates="books") #relationship to link with Category table backpopulate is used for bidirectional relationship
    borrows=relationship("Borrow", back_populates="book") #relationship to link with Borrow table
    
class Borrow(Base): #to track borrowed books
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id")) #foreign key to link with Book table
    borrow_date = Column(Date)
    return_date = Column(Date)
    book = relationship("Book", back_populates="borrows") #relationship to link with Book table backpopulate is used for bidirectional relationship
    
class Limit(Base): #to set monthly borrow limit
    __tablename__ = "limits"
    id = Column(Integer, primary_key=True)
    month = Column(String)
    max_books=Column(Integer) #maximum books that can be borrowed in a month
    
def add_category(): #to add book category
    name=input("category name: ")
    #create category object and save to database
    session.add((Category(name=name))) #create a new Category object with the provided name and add it to the current database session using session.add(). This prepares the new category for insertion into the database when 
    session.commit() #commit is used to save the changes made to the database. When you add a new Category object to the session using session.add(), it is not immediately saved to the database. The session.commit() method is called to persist the changes, which means that the new category will be inserted into the categories table in the databa
    print("Category added")
    
def add_book(): #to add new book
    title=input("book title: ")
    author=input("book author: ")
    category_id=int(input("Category ID: "))
    #create book
    session.add((Book(title=title, author=author, category_id=category_id))) #create a new Book object with the provided title, author, and category_id. The session.add() method is used to add this new Book object to the current database session, which prepares it for insertion into the database when session.commit() is called.
    session.commit()
    
def borrow_book(): #to borrow a book
    book_id=int(input("Book ID: "))
    date=input("borrow date (YYYY-MM-DD): ")
    #create borrow record
    session.add((Borrow(book_id=book_id, borrow_date=date))) 
    session.commit()
    print("book borrowed")
    
def update_borrow(): #to update borrow date
    bid=int(input("borrow id: "))
    #find borrow record
    borrow=session.query(Borrow).filter_by(id=bid).first()
    if borrow:
        borrow.borrow_date=input("new date: ")
        session.commit()
        print("borrow date updated")
    else:
        print("borrow record not found")
        
def delete_borrow(): #to delete borrow record
    bid=int(input("borrow id: "))
    borrow=session.query(Borrow).filter_by(id=bid).first() #
    if borrow:
        session.delete(borrow)
        session.commit()
        print("borrow record deleted")
    else:
        print("borrow record not found")
        
def search_by_date(): #to find borrowed books by date
    date=input("enter date: ")
    borrows=session.query(Borrow).filter_by(Borrow.borrow_date==date).all() #filter_by is used to filter records based on specific criteria. In this case, we are filtering the Borrow records where the borrow_date matches the input date. The all() method retrieves all matching records as a list.
    for b in borrows:
        print(b.book.title,"-",b.book.date)
        
#create all tables
Base.metadata.create_all(engine)
print("Tables created successfully")