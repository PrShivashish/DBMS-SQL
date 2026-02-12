# 🗄️ DBMS & SQL Mastery: The Code Vault

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Learning-success?style=for-the-badge)

> **"Data is the new oil? No, Data is the new soil."** 🌱
> Welcome to my digital laboratory for mastering Database Management Systems, SQL queries, and Python ORM integration.

---

## 🚀 About This Repository

This isn't just a collection of scripts; it's a **roadmap**. This repository documents the journey from writing raw `SELECT * FROM` queries to building full-fledged, object-oriented database applications using **SQLAlchemy**.

Whether you are looking for basic syntax, complex subqueries, or a complete Finance Tracker backend, you've parked at the right dock. ⚓

### 🎯 What's Inside?
* **Raw SQL & Logic**: Deep dives into Constraints, Joins, Normalization, and ACID properties.
* **Python Connectors**: Bridging the gap between code and data with `mysql-connector` and `psycopg2`.
* **ORM Magic**: Mastering **SQLAlchemy** to treat database tables like Python classes.
* **Real Projects**: Functional backends for Finance and Library management.

---

## 📂 The Arsenal (Repository Structure)

### 1️⃣ 🧠 The Knowledge Base (Jupyter Notebooks)
*Interactive notebooks containing theory, syntax, and execution examples.*

| File | Description | Key Concepts |
| :--- | :--- | :--- |
| **`DBMS_Basics.ipynb`** | The Foundation | `CREATE`, `INSERT`, `UPDATE`, `DELETE`, `GROUP BY`, Aggregate Functions. |
| **`SQL_Constraints_SUBQUERY.ipynb`** | The Advanced Stuff | Primary/Foreign Keys, `JOINS` (Inner, Left, Right), Subqueries, Indexing, Normalization. |

### 2️⃣ 🛠️ The Tool Belt (Python Scripts)
*Essential scripts for connectivity and basic operations.*

* **`Employee.py`**: A raw SQL approach to managing Employee and Project relationships.
* **`Employee_orm.py`**: The same logic evolved! Uses **SQLAlchemy ORM** to perform CRUD operations without writing a single line of raw SQL.
* **`db_test.py`**: A connection tester for MySQL.
* **`psycopg.py`**: A connection tester for PostgreSQL (Postgres).
* **`table_creation.py`**: Exploring `One-to-Many` relationships with SQLAlchemy.

---

## 🌟 Featured Projects

### 💰 FinTrack Pro (`Fintrack_pro.py`)
*A Personal Finance Manager Backend*

Stop wondering where your money went. **FinTrack Pro** is a Python-based expense tracker powered by SQLAlchemy.

* **Key Features:**
    * 📂 **Category Management**: Add and organize custom expense categories.
    * 💸 **Expense Logging**: Add expenses with titles, amounts, and dates.
    * 🔄 **Subscription Tracker**: Never miss a renewal date again.
    * 📉 **Budget Enforcer**: Set monthly limits and get alerts when you overspend!
    * 📊 **Reports**: Generate category-wise expenditure reports using raw SQL aggregations within the ORM.

### 📚 LibTrack (`Library_management_sqlalchemy_project.py`)
*A Smart Library Management System*

A robust backend system to manage book circulation and inventory.

* **Key Features:**
    * 📖 **Cataloging**: Add books and assign them to specific categories.
    * 🤝 **Borrowing System**: Track who borrowed what and when.
    * 📅 **Due Dates**: Update borrow dates and manage returns.
    * 🛡️ **Borrow Limits**: Enforce maximum book borrowing limits per month.

---

## ⚡ Tech Stack & Tools

* **Languages:** Python 🐍, SQL 💾
* **Databases:** SQLite (for portability), MySQL, PostgreSQL
* **Libraries:**
    * `sqlalchemy` (The star of the show)
    * `mysql-connector-python`
    * `psycopg2`
    * `ipython-sql`

---

## 🏃‍♂️ How to Run

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/your-username/DBMS-SQL.git](https://github.com/your-username/DBMS-SQL.git)
    cd DBMS-SQL
    ```

2.  **Install Dependencies:**
    ```bash
    pip install sqlalchemy mysql-connector-python psycopg2-binary notebook
    ```

3.  **Run a Project (e.g., FinTrack Pro):**
    ```bash
    python Fintrack_pro.py
    ```
    *Follow the on-screen prompts to add expenses, set budgets, and view reports!*

---

## 🧪 Visualizing the Data (ER Diagram)

If you were to visualize the **FinTrack Pro** database schema, it would look something like this:

```mermaid
erDiagram
    CATEGORIES ||--o{ EXPENSES : contains
    CATEGORIES {
        int id PK
        string name
    }
    EXPENSES {
        int id PK
        string title
        int amount
        date date
        int category_id FK
    }
    BUDGETS {
        int id PK
        string month
        int limit
    }
    SUBSCRIPTIONS {
        int id PK
        string name
        int amount
        date next_date
    }
