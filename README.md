# FinTrack Pro - Personal Finance Tracker

A personal finance tracking application built with Python and SQLAlchemy ORM that helps users manage expenses, subscriptions, categories, and budgets using an SQLite database.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Database Schema](#database-schema)
- [Application Flow](#application-flow)
- [Function Documentation](#function-documentation)
- [Usage Examples](#usage-examples)
- [Dependencies](#dependencies)
- [Installation](#installation)

## 🎯 Overview

FinTrack Pro is a command-line personal finance management system that allows users to:
- Track daily expenses with categories
- Manage recurring subscriptions
- Set and monitor monthly budgets
- Generate category-wise expense reports
- Search expenses by date

## ✨ Features

- **Expense Management**: Add, update, and delete expense records
- **Category System**: Organize expenses into custom categories
- **Subscription Tracking**: Monitor recurring subscription payments
- **Budget Control**: Set monthly limits and get alerts when exceeded
- **Reporting**: Generate category-wise spending reports using raw SQL
- **Date-based Search**: Find expenses by specific dates
- **SQLAlchemy ORM**: Efficient database operations with object-relational mapping

## 🗄️ Database Schema

The application uses SQLite database with the following tables:

### Categories Table
```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name STRING
);
```

### Expenses Table
```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    title STRING,
    amount INTEGER,
    date STRING,
    category_id INTEGER FOREIGN KEY REFERENCES categories(id)
);
```

### Subscriptions Table
```sql
CREATE TABLE subscriptions (
    id INTEGER PRIMARY KEY,
    name STRING,
    amount INTEGER,
    next_date STRING
);
```

### Budgets Table
```sql
CREATE TABLE budgets (
    id INTEGER PRIMARY KEY,
    month STRING,
    limit INTEGER
);
```

## 🔄 Application Flow

### 1. **Database Initialization**
```python
engine = create_engine("sqlite:///fintrack.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
```
- Creates SQLite database connection
- Sets up SQLAlchemy session for database operations
- Establishes ORM base class for all models

### 2. **Model Definition**
The application defines four main ORM models with relationships:
- **Category ↔ Expense**: One-to-many relationship (one category can have multiple expenses)
- Each model inherits from `Base` and maps to corresponding database table

### 3. **Core Operations Flow**

#### **Setup Phase**
1. Initialize database engine and session
2. Define ORM models with relationships
3. Create all tables in database

#### **User Interaction Phase**
1. **Category Management**: Users first create expense categories
2. **Expense Tracking**: Add expenses linked to categories
3. **Subscription Management**: Track recurring payments
4. **Budget Planning**: Set monthly spending limits
5. **Monitoring & Reporting**: Check budget status and generate reports

## 📚 Function Documentation

### Category Management
- **`add_category()`**: Creates new expense categories for better organization

### Expense Operations
- **`add_expense()`**: Records new expenses with title, amount, date, and category
- **`update_expense()`**: Modifies existing expense amounts by ID
- **`delete_expense()`**: Removes expense records from database
- **`search_by_date()`**: Retrieves all expenses for a specific date

### Subscription Management
- **`add_subscription()`**: Tracks recurring payments with next due dates

### Budget Control
- **`set_budget()`**: Establishes monthly spending limits
- **`check_budget()`**: Compares actual spending against set limits and provides alerts

### Reporting
- **`category_report()`**: Generates category-wise spending summary using raw SQL with JOINs and GROUP BY

## 💡 Usage Examples

### Basic Workflow Example

1. **First-time Setup**
   ```python
   # Application automatically creates tables on startup
   add_category()  # Add categories like "Food", "Transport", "Entertainment"
   set_budget()    # Set monthly budget limit
   ```

2. **Daily Usage**
   ```python
   add_expense()       # Record daily expenses
   add_subscription()  # Track new subscriptions
   search_by_date()    # Look up expenses from specific dates
   ```

3. **Monthly Review**
   ```python
   category_report()   # See spending breakdown by category
   check_budget()      # Check if monthly limit was exceeded
   ```

### Sample Data Flow
```
User Input → SQLAlchemy ORM → SQLite Database
    ↓              ↓               ↓
Category: "Food" → Category Object → categories table
Expense: "$25 Lunch" → Expense Object → expenses table
Budget: "$500 Jan" → Budget Object → budgets table
```

## 🔧 Technical Implementation Details

### ORM Relationships
- **Foreign Key Constraint**: `category_id` in expenses links to categories
- **Bidirectional Relationship**: `back_populates` enables navigation between related objects
- **Session Management**: All database operations use SQLAlchemy session for transaction control

### Data Validation
- Input validation through type conversion (int(), string input)
- Database constraints ensure data integrity
- Error handling for missing records

### Raw SQL Integration
- `category_report()` uses raw SQL with `text()` for complex aggregation
- Demonstrates both ORM and raw SQL capabilities in same application

## 📦 Dependencies

- **SQLAlchemy**: ORM framework for database operations
- **SQLite**: Lightweight database engine (no additional installation required)

## 🚀 Installation

1. **Install SQLAlchemy**:
   ```bash
   pip install sqlalchemy
   ```

2. **Run the Application**:
   ```python
   python Fintrack_pro.py
   ```

3. **Database Creation**:
   - SQLite database `fintrack.db` is automatically created in the same directory
   - All tables are created on first run

## 🏗️ Architecture Benefits

- **ORM Advantages**: Object-oriented database interactions, automatic SQL generation
- **Relationship Mapping**: Easy navigation between related data entities  
- **Transaction Safety**: Automatic commit/rollback functionality
- **Scalability**: Easy to extend with additional features and tables
- **Data Integrity**: Foreign key constraints maintain referential integrity

## 🔮 Future Enhancements

- Add GUI interface using Tkinter or web framework
- Implement user authentication and multiple user support
- Add data visualization with charts and graphs
- Include expense import/export functionality
- Implement more sophisticated date filtering and reporting

---

**Note**: This application demonstrates fundamental concepts of database design, ORM usage, and personal finance management system architecture using Python and SQLAlchemy.