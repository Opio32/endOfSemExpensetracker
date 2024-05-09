import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("expensetracker.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create table for expenses
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                date TEXT,
                category TEXT,
                description TEXT,
                amount REAL
            )
        """)

    def add_expense(self, date, category, description, amount):
        # Add expense to database
        self.cursor.execute("""
            INSERT INTO expenses (date, category, description, amount)
            VALUES (?, ?, ?, ?)
        """, (date, category, description, amount))
        self.conn.commit()

    def get_summary(self):
        # Get summary of expenses by category
        self.cursor.execute("""
            SELECT category, SUM(amount) AS total_amount
            FROM expenses
            GROUP BY category
        """)
        result = self.cursor.fetchall()

        summary = ""
        for row in result:
            summary += f"Category: {row[0]}, Total Amount: {row[1]:.2f}\n"
        return summary

    def __del__(self):
        self.conn.close()