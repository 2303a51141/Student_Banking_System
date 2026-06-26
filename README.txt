# 🏦 Student Banking System

<p align="center">
  <img src="screenshots/07-dashboard-after-deposit.png" alt="Student Banking System" width="90%">
</p>

<p align="center">
  <b>A Full-Stack Banking Web Application built with Python Flask, MySQL, HTML, CSS, and JavaScript.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/MySQL-Database-blue?logo=mysql" alt="MySQL">
  <img src="https://img.shields.io/badge/HTML5-orange?logo=html5" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-blue?logo=css3" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-yellow?logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/Render-Live-success" alt="Render">
</p>

---

# 🌐 Live Demo

🔗 **https://student-banking-system.onrender.com**

---

# 📖 Project Overview

The **Student Banking System** is a secure and responsive full-stack web application that simulates the core functionality of an online banking system.

Developed using **Python Flask** and **MySQL**, the application enables users to register, authenticate securely, create bank accounts, deposit and withdraw money, check balances, and view transaction history through a clean and intuitive interface.

This project was built as a **Final Year B.Tech Computer Science & Engineering Project** to demonstrate full-stack web development, authentication, database integration, CRUD operations, and deployment.

---

# ✨ Features

* 👤 User Registration
* 🔐 Secure Login & Logout
* 🏦 Create Savings Account
* 🏦 Create Current Account
* 💰 Deposit Funds
* 💸 Withdraw Funds
* 💳 Check Account Balance
* 📜 View Transaction History
* 🔒 Session-Based Authentication
* ✅ Input Validation
* 📱 Responsive User Interface

---

# 🛠️ Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend Programming       |
| Flask      | Web Framework             |
| MySQL      | Database                  |
| HTML5      | Frontend Structure        |
| CSS3       | Styling                   |
| JavaScript | Client-side Functionality |
| Render     | Cloud Deployment          |

---

# 📂 Project Structure

```text
student-banking-system/
│
├── app.py
├── schema.sql
├── requirements.txt
├── Procfile
├── README.md
├── LICENSE
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── create_account.html
│   ├── deposit.html
│   ├── withdraw.html
│   ├── balance.html
│   ├── transactions.html
│   └── admin.html
│
└── screenshots/
```

---

# 🖼️ Application Screenshots

## 📝 Registration Page

![Registration Page](screenshots/01-registration-page.png)

---

## 🔑 Login Page

![Login Page](screenshots/02-login-page.png)

---

## 🏦 Dashboard (No Account)

![Dashboard No Account](screenshots/03-dashboard-no-account.png)

---

## 📝 Create Bank Account

![Create Bank Account](screenshots/04-create-bank-account.png)

---

## 📊 Dashboard

![Dashboard](screenshots/05-dashboard-initial.png)

---

## 💰 Deposit Money

![Deposit Money](screenshots/06-deposit-money.png)

---

## 📈 Dashboard After Deposit

![Dashboard After Deposit](screenshots/07-dashboard-after-deposit.png)

---

## 💸 Withdraw Money

![Withdraw Money](screenshots/08-withdraw-money.png)

---

## 📉 Dashboard After Withdrawal

![Dashboard After Withdrawal](screenshots/09-dashboard-after-withdraw.png)

---

## 💳 Account Balance

![Account Balance](screenshots/10-account-balance.png)

---

## 📜 Transaction History

![Transaction History](screenshots/11-transaction-history.png)

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/2303a51141/Student_Banking_System.git
```

## 2️⃣ Navigate to the Project Directory

```bash
cd Student_Banking_System
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Configure the Database

* Install MySQL.
* Create a database.
* Import the `schema.sql` file.
* Update your MySQL credentials in `app.py`.

## 5️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🗄️ Database Design

```text
Users
│
├── user_id
├── username
├── password
└── created_at

        │

        ▼

Accounts
│
├── account_number
├── account_type
├── balance
└── user_id

        │

        ▼

Transactions
│
├── transaction_id
├── account_number
├── transaction_type
├── amount
└── transaction_date
```

---

# 🔄 Application Workflow

```text
Register
     │
     ▼
Login
     │
     ▼
Dashboard
     │
     ▼
Create Account
     │
     ▼
Deposit / Withdraw
     │
     ▼
Check Balance
     │
     ▼
View Transaction History
```

---

# 🎯 Learning Outcomes

During the development of this project, I gained practical experience in:

* Full-Stack Web Development
* Flask Framework
* MySQL Database Integration
* Authentication & Authorization
* Session Management
* CRUD Operations
* Database Design
* Responsive UI Development
* Deployment using Render
* Software Engineering Best Practices

---

# 🚀 Future Enhancements

* 💸 Money Transfer Between Users
* 📧 Email Notifications
* 🔑 Password Reset
* 📱 OTP Verification
* 📄 PDF Account Statements
* 🌐 REST API Integration
* 🔐 JWT Authentication
* 🛡️ Two-Factor Authentication

---

# 👨‍💻 Author

**Mani Teja Patel Jarathi**

🎓 B.Tech Computer Science & Engineering
🏫 SR University

### 📬 Connect with Me

* **GitHub:** https://github.com/2303a51141
* **LinkedIn:** https://www.linkedin.com/in/mani-teja-patel-jarathi
* **Portfolio:** https://portfolio-mani00.vercel.app

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📜 License

This project is licensed under the **MIT License**.

---

<p align="center">
Made with ❤️ using Python, Flask, MySQL, HTML, CSS and JavaScript.
</p>
