#FLOW:  Functions to be made for FinTrack Pro using SQLAlchemy:
# add_category() --> add expense category
# add_expense() --> add new Expense
# add_subscription() --> add new Subscription
# update_expense() --> update expense details
# delete_expense() --> delete expense record
# search_by_date() --> find expenses by date
# category_report() --> category wise total (Raw SQL)
# set_budget() --> set monthly budget limit
# check_budget() --> check if limit exceeded

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


#database connection
engine = create_engine("sqlite:///fintrack.db")
Base=declarative_base()
Session=sessionmaker(bind=engine) 
session=Session()      #all these for insertion and retrieval of data from database

class Category(Base):  #Base is the base class for all our ORM models. It provides the necessary functionality to define tables and map them to Python classes.
    __tablename__ = "categories"  #__tablename__ is a special attribute that specifies the name of the table in the database that this class will be mapped to. 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    expenses=relationship("Expense", back_populates="category") #relationship to link with Expense table backpopulate is used for bidirectional relationship
    
class Expense(Base): #to store expense details     
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Integer)
    date = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id")) #foreign key to link with Category table
    category = relationship("Category", back_populates="expenses") #relationship to link with Category table backpopulate is used for bidirectional relationship
    
class Subscription(Base): #to track subscriptions
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Integer)
    next_date = Column(String)

class Budget(Base): #to set monthly budget limit
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True)
    month = Column(String)
    limit = Column(Integer) #maximum amount that can be spent in a month
    
def add_category(): #to add expense category
    name=input("category name: ")
    #create category object and save to database
    session.add((Category(name=name))) 
    session.commit() #commit is used to save the changes made to the database. 
    print("Category added")
    
def add_expense(): #to add new expense
    title=input("expense title: ")
    amount=int(input("amount: "))
    date=input("date (YYYY-MM-DD): ")
    category_id=int(input("Category ID: "))
    #create expense obj
    session.add((Expense(title=title, amount=amount, date=date, category_id=category_id))) 
    session.commit()
    print("Expense added")

def add_subscription(): #to add new subscription
    name=input("subscription name: ")
    amount=int(input("amount: "))
    next_date=input("next due date (YYYY-MM-DD): ")
    #create subscription
    session.add((Subscription(name=name, amount=amount, next_date=next_date)))
    session.commit()
    print("Subscription added")
    
def update_expense(): #to update expense details
    eid=int(input("expense id: "))
    #find expense record
    expense=session.query(Expense).filter_by(id=eid).first()
    if expense:
        expense.amount=int(input("new amount: "))
        session.commit()
        print("expense updated")
    else:
        print("expense record not found")
        
def delete_expense(): #to delete expense record
    eid=int(input("expense id: "))
    expense=session.query(Expense).filter_by(id=eid).first() #
    if expense:
        session.delete(expense)
        session.commit()
        print("expense record deleted")
    else:
        print("expense record not found")
        
def search_by_date(): #to find expenses by date
    date=input("enter date: ")
    expenses=session.query(Expense).filter(Expense.date==date).all() #filter is used to apply condition using model field comparison
    for e in expenses:
        print(e.title,"-",e.amount)

def category_report(): #category wise total using Raw SQL as requested in objectives
    #executing raw sql query for aggregation
    sql = text("SELECT c.name, SUM(e.amount) FROM categories c JOIN expenses e ON c.id = e.category_id GROUP BY c.name")
    result = session.execute(sql) #run raw SQL queries directly against the database
    print("Category Wise Expenditure:")
    for row in result:
        print(row[0], ":", row[1])

def set_budget(): #to set monthly budget
    month=input("month (e.g., Jan): ")
    limit=int(input("limit amount: "))
    #create budget record
    session.add((Budget(month=month, limit=limit)))
    session.commit()
    print("Budget set")

def check_budget(): #alert when limit exceeded
    month_check=input("enter month to check: ")
    budget=session.query(Budget).filter_by(month=month_check).first()
    if budget:
        #calculating total expenses for this month (simplified logic for demo)
        total_spent = 0
        expenses = session.query(Expense).all() #In a real scenario we would filter by date string matching the month
        for e in expenses:
             if month_check in e.date: #simple string check if month is in date
                 total_spent += e.amount
        
        print(f"Total Spent: {total_spent}, Budget Limit: {budget.limit}")
        if total_spent > budget.limit:
            print("ALERT: Budget Exceeded!")
        else:
            print("Within Budget")
    else:
        print("No budget found for this month")
        
#create all tables
Base.metadata.create_all(engine)
print("Tables created successfully")