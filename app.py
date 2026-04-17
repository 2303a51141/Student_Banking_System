# Bank Management System
# Final Year Project
# Backend: Flask + SQLite

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3
import os
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "my_bank_secret_key_123"  # secret key for session

DB_NAME = "bank.db"


# ---------------- Database Helper ----------------
def get_db():
    # connect to sqlite database
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    # create tables if they don't exist (runs schema.sql)
    if not os.path.exists(DB_NAME):
        conn = get_db()
        with open("schema.sql", "r") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print("Database created successfully.")


# ---------------- Routes ----------------

@app.route("/")
def home():
    # if user logged in, go to dashboard, else login page
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


# ---------- Register ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"].strip()
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        # simple validation
        if not name or not username or not password:
            flash("Please fill all fields", "error")
            return redirect(url_for("register"))

        if len(password) < 4:
            flash("Password must be at least 4 characters", "error")
            return redirect(url_for("register"))

        conn = get_db()
        cur = conn.cursor()

        # check if username already exists
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if cur.fetchone():
            flash("Username already exists", "error")
            conn.close()
            return redirect(url_for("register"))

        # insert new user
        cur.execute(
            "INSERT INTO users (name, username, password, role) VALUES (?, ?, ?, ?)",
            (name, username, password, "user")
        )
        conn.commit()
        conn.close()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


# ---------- Login ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            # save user info in session
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["name"] = user["name"]
            session["role"] = user["role"]
            flash("Login successful", "success")

            if user["role"] == "admin":
                return redirect(url_for("admin"))
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------- Logout ----------
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out", "success")
    return redirect(url_for("login"))


# ---------- Dashboard ----------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts WHERE user_id=?", (session["user_id"],))
    account = cur.fetchone()
    conn.close()

    return render_template("dashboard.html", account=account)


# ---------- Create Account ----------
@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()

    # check if account already exists
    cur.execute("SELECT * FROM accounts WHERE user_id=?", (session["user_id"],))
    existing = cur.fetchone()
    if existing:
        flash("You already have a bank account", "error")
        conn.close()
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        acc_type = request.form["acc_type"]

        # generate random 10 digit account number
        acc_number = str(random.randint(1000000000, 9999999999))

        cur.execute(
            "INSERT INTO accounts (user_id, account_number, account_type, balance) VALUES (?, ?, ?, ?)",
            (session["user_id"], acc_number, acc_type, 0.0)
        )
        conn.commit()
        conn.close()

        flash("Bank account created! Account No: " + acc_number, "success")
        return redirect(url_for("dashboard"))

    conn.close()
    return render_template("create_account.html")


# ---------- Deposit ----------
@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts WHERE user_id=?", (session["user_id"],))
    account = cur.fetchone()

    if not account:
        flash("Please create a bank account first", "error")
        conn.close()
        return redirect(url_for("create_account"))

    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
        except ValueError:
            flash("Please enter a valid amount", "error")
            conn.close()
            return redirect(url_for("deposit"))

        if amount <= 0:
            flash("Amount must be greater than zero", "error")
            conn.close()
            return redirect(url_for("deposit"))

        new_balance = account["balance"] + amount

        # update balance
        cur.execute("UPDATE accounts SET balance=? WHERE id=?", (new_balance, account["id"]))

        # save transaction
        cur.execute(
            "INSERT INTO transactions (account_id, type, amount, date) VALUES (?, ?, ?, ?)",
            (account["id"], "Deposit", amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        conn.commit()
        conn.close()

        flash("Deposit successful! New balance: " + str(new_balance), "success")
        return redirect(url_for("dashboard"))

    conn.close()
    return render_template("deposit.html", account=account)


# ---------- Withdraw ----------
@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts WHERE user_id=?", (session["user_id"],))
    account = cur.fetchone()

    if not account:
        flash("Please create a bank account first", "error")
        conn.close()
        return redirect(url_for("create_account"))

    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
        except ValueError:
            flash("Please enter a valid amount", "error")
            conn.close()
            return redirect(url_for("withdraw"))

        if amount <= 0:
            flash("Amount must be greater than zero", "error")
            conn.close()
            return redirect(url_for("withdraw"))

        # check insufficient balance
        if amount > account["balance"]:
            flash("Insufficient balance!", "error")
            conn.close()
            return redirect(url_for("withdraw"))

        new_balance = account["balance"] - amount

        cur.execute("UPDATE accounts SET balance=? WHERE id=?", (new_balance, account["id"]))
        cur.execute(
            "INSERT INTO transactions (account_id, type, amount, date) VALUES (?, ?, ?, ?)",
            (account["id"], "Withdraw", amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        conn.commit()
        conn.close()

        flash("Withdraw successful! New balance: " + str(new_balance), "success")
        return redirect(url_for("dashboard"))

    conn.close()
    return render_template("withdraw.html", account=account)


# ---------- Balance ----------
@app.route("/balance")
def balance():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts WHERE user_id=?", (session["user_id"],))
    account = cur.fetchone()
    conn.close()

    return render_template("balance.html", account=account)


# ---------- Transaction History ----------
@app.route("/transactions")
def transactions():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts WHERE user_id=?", (session["user_id"],))
    account = cur.fetchone()

    txns = []
    if account:
        cur.execute("SELECT * FROM transactions WHERE account_id=? ORDER BY id DESC", (account["id"],))
        txns = cur.fetchall()
    conn.close()

    return render_template("transactions.html", txns=txns, account=account)


# ---------- Admin View ----------
@app.route("/admin")
def admin():
    if "user_id" not in session or session.get("role") != "admin":
        flash("Admin access only", "error")
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.id, u.name, u.username, a.account_number, a.account_type, a.balance
        FROM users u
        LEFT JOIN accounts a ON u.id = a.user_id
        WHERE u.role='user'
    """)
    users = cur.fetchall()
    conn.close()

    return render_template("admin.html", users=users)


# ---------------- Run ----------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
