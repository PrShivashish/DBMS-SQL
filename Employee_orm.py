from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import or_, and_
from sqlalchemy import desc, asc

# step 1 : create database connection
engine = create_engine("sqlite:///company.db")

# step 2 : base class
Base = declarative_base()

# step 3 : table creation
class Employee(Base):
    __tablename__ = "Employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)

# step 4 : create table if not exists
Base.metadata.create_all(engine)

# step 5 : create session
Session = sessionmaker(bind=engine)
session = Session()

# ---------------- ADD EMPLOYEE ----------------
# run this block only once (comment later)
e1 = Employee(name="Nobita", age=14, department="berojgar")
e2 = Employee(name="Zian", age=15, department="rojgar")
e3 = Employee(name="Shivashish", age=21, department="Ameer")
e4 = Employee(name="Om", age=25, department="Gareeb")

session.add_all([e1, e2, e3, e4])
# print("Employees added")

# -------------UPDATE EMPLOYEE----------------
# emp = session.query(Employee).filter_by(id=1).first()
# emp.name = "Sizuka"
# session.commit()
# print("Employee value updated successfully")

# ---------------- DELETE ALL EMPLOYEE ----------------
# removes all rows from table
# session.query(Employee).delete()
# session.commit()  # IMPORTANT: Commit immediately to actually delete from DB
# print("All employees deleted")


# # ---------------- DELETE SPECIFIC ----------------
# emp=session.query(Employee).filter_by(id=2).first()
# if emp:                             
#     session.delete(emp)   
# print("Given employee deleted")


# # ---------------- AND CONDITION ----------------
# name = Nobita AND age > 13
and_result = session.query(Employee).filter(and_(Employee.name == "Nobita",Employee.age > 13)).all()

print("AND condition result:")
for i in and_result:
    print(i.id, i.name, i.age, i.department)

# # ---------------- OR CONDITION ----------------
# # name = Om OR age < 18
# or_result = session.query(Employee).filter(or_(Employee.name == "Om",Employee.age < 18)).all()

# print("OR condition result:")
# for i in or_result:
#     print(i.id, i.name, i.age, i.department)

# # ---------------- ONE / ONE_OR_NONE ----------------
# # fetch exactly one or none
# emp = session.query(Employee).filter(Employee.age > 18).one_or_none()
# if emp:
#     print("One_or_none result:", emp.id, emp.name, emp.age, emp.department)
# else:
#     print("No employee found for one_or_none")

# # ----------------ORDER BY----------------------
# #ASC
# order_asc = session.query(Employee).order_by(Employee.age).all()

# print("Order By Age (ASC):")
# for i in order_asc:
#     print(i.id, i.name, i.age, i.department)

# #DSC
# order_desc = session.query(Employee).order_by(Employee.age.desc()).all()

# print("Order By Age (DESC):")
# for i in order_desc:
#     print(i.id, i.name, i.age, i.department)
    
# # ---------------LIMIT----------------
# limit_result=session.query(Employee).order_by(Employee.id).limit(2).all()
# print("Limit result:")
# for i in limit_result:
#     print(i.id, i.name, i.age, i.department)

# ---------------- SAVE ALL CHANGES ----------------
session.commit()

# ---------------- FETCH & PRINT (AT LAST) ----------------
employee_list = session.query(Employee).all()
print("\nFinal Employee Table Data:")
for i in employee_list:
    print(i.id, i.name, i.age, i.department)