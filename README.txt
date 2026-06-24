==================================================
        BANK MANAGEMENT SYSTEM
        Final Year Project
==================================================

PROJECT TITLE:
    Bank Management System

DESCRIPTION:
    A simple web-based Bank Management System built using
    Python (Flask) and MYSQL database. The system allows
    users to register, login, create a bank account,
    deposit money, withdraw money, view balance, and check
    transaction history. An admin user can view all users
    and accounts.

--------------------------------------------------
TECHNOLOGIES USED:
--------------------------------------------------
    - Frontend : HTML, CSS, JavaScript
    - Backend  : Python (Flask framework)
    - Database : MYSQL

--------------------------------------------------
FEATURES:
--------------------------------------------------
    1. User Registration
    2. User Login / Logout (with session handling)
    3. Create a Bank Account (Savings / Current)
    4. Deposit Money
    5. Withdraw Money (with insufficient balance check)
    6. Check Account Balance
    7. View Transaction History
    8. Admin Panel (view all users & accounts)
    9. Simple input validation
   10. Clean and responsive user interface

--------------------------------------------------
PROJECT STRUCTURE:
--------------------------------------------------
    BankManagementSystem/
        app.py              -> Main Flask application
        schema.sql          -> Database schema (SQL script)
        bank.db             -> MYSQL database (auto created)
        README.txt          -> Project documentation
        static/
            style.css       -> Stylesheet
        templates/
            base.html
            login.html
            register.html
            dashboard.html
            create_account.html
            deposit.html
            withdraw.html
            balance.html
            transactions.html
            admin.html

--------------------------------------------------
HOW TO RUN THE PROJECT (STEP-BY-STEP):
--------------------------------------------------
1. Install Python  (if not already installed).

2. Install Flask using pip:
       pip install flask

3. Open a terminal/command prompt inside the
   project folder "BankManagementSystem".

4. Run the application:
       python app.py

5. The first time you run, the database (bank.db)
   will be created automatically using schema.sql.

6. Open your web browser and visit:
       https://student-banking-system.onrender.com

--------------------------------------------------
SAMPLE TEST DATA (already inserted in database):
--------------------------------------------------
   Admin Login:
       Username : admin
       Password : admin123

   Sample User Login:
       Username : john
       Password : john123
       Account No: 1234567890
       Balance  : $5000

--------------------------------------------------
NOTES:
--------------------------------------------------
   - Passwords are stored in plain text for project
     simplicity. In a real system, they should be
     hashed (e.g., using bcrypt).
   - This project is developed for academic purposes.

==================================================
