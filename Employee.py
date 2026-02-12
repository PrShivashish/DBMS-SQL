# Employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,      # employee id
    emp_name VARCHAR(50),        # employee name
    department VARCHAR(50)       # department
);

# Insert employees data
INSERT INTO employees VALUES
(1,'Rahul','IT'),
(2,'Neha','HR'),
(3,'Amit','IT'),
(4,'Priya','Finance'),
(5,'Karan','HR');


# Projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY,  # project id
    project_name VARCHAR(50),    # project name
    budget INT                   # project budget
);

# Insert projects data
INSERT INTO projects VALUES
(101,'Website Revamp',100000),
(102,'Mobile App',150000),
(103,'Payroll System',80000);


# Employee–Project mapping table
CREATE TABLE employee_projects (
    emp_id INT,                  # employee id
    project_id INT,              # project id
    hours_worked INT,            # hours worked
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

# Insert employee-project data
INSERT INTO employee_projects VALUES
(1,101,40),
(1,102,30),
(2,103,20),
(3,101,50),
(3,102,25),
(4,103,35),
(5,103,30);


# # Q1: Total hours worked by each employee
# SELECT e.emp_id, e.emp_name, SUM(ep.hours_worked) AS total_hours FROM employees e JOIN employee_projects ep ON e.emp_id = ep.emp_id GROUP BY e.emp_id, e.emp_name;


# # Q2: Total hours spent on each project
# SELECT p.project_id, p.project_name, SUM(ep.hours_worked) AS total_hours FROM projects p JOIN employee_projects ep ON p.project_id = ep.project_id GROUP BY p.project_id, p.project_name;


# # Q3: Department-wise total working hours
# SELECT e.department, SUM(ep.hours_worked) AS total_hours FROM employees e JOIN employee_projects ep ON e.emp_id = ep.emp_id GROUP BY e.department;