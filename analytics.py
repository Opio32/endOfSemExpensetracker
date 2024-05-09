from database import Database

class Analytics:
    def __init__(self, db):
        self.db = db

    def get_analytics(self):
        # Provide analytics based on expense data
        self.db.cursor.execute("""
            SELECT category, COUNT(*) AS num_expenses, SUM(amount) AS total_amount
            FROM expenses
            GROUP BY category
        """)
        result = self.db.cursor.fetchall()

        analytics = "Analytics Report\n"
        analytics += "-----------------\n"
        for row in result:
            analytics += f"Category: {row[0]}, Number of Expenses: {row[1]}, Total Amount: {row[2]:.2f}\n"
        
        return analytics
