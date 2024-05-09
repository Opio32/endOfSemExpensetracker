import tkinter as tk
from tkinter import messagebox
from analytics import Analytics

class GUI:
    def __init__(self, db):
        self.db = db
        self.root = tk.Tk()
        self.root.title("ExpenseTracker")
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for adding expenses, viewing summary, and analytics
        self.add_expense_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.summary_button = tk.Button(self.root, text="View Summary", command=self.view_summary)
        self.analytics_button = tk.Button(self.root, text="Analytics", command=self.view_analytics)

        self.add_expense_button.pack()
        self.summary_button.pack()
        self.analytics_button.pack()

    def add_expense(self):
        # Create a new window for adding expenses
        self.add_expense_window = tk.Toplevel(self.root)
        self.add_expense_window.title("Add Expense")
        self.create_add_expense_widgets()

    def create_add_expense_widgets(self):
        # Create widgets for entering expense details
        self.date_label = tk.Label(self.add_expense_window, text="Date")
        self.date_entry = tk.Entry(self.add_expense_window)
        self.category_label = tk.Label(self.add_expense_window, text="Category")
        self.category_entry = tk.Entry(self.add_expense_window)
        self.description_label = tk.Label(self.add_expense_window, text="Description")
        self.description_entry = tk.Entry(self.add_expense_window)
        self.amount_label = tk.Label(self.add_expense_window, text="Amount")
        self.amount_entry = tk.Entry(self.add_expense_window)
        self.add_button = tk.Button(self.add_expense_window, text="Add", command=self.add_expense_to_db)

        self.date_label.pack()
        self.date_entry.pack()
        self.category_label.pack()
        self.category_entry.pack()
        self.description_label.pack()
        self.description_entry.pack()
        self.amount_label.pack()
        self.amount_entry.pack()
        self.add_button.pack()

    def add_expense_to_db(self):
        # Add expense to database
        date = self.date_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        self.db.add_expense(date, category, description, amount)
        self.add_expense_window.destroy()

    def view_summary(self):
        # Create a new window for viewing summary
        self.summary_window = tk.Toplevel(self.root)
        self.summary_window.title("Summary")
        self.create_summary_widgets()

    def create_summary_widgets(self):
        # Create widgets for displaying summary
        self.summary_text = tk.Text(self.summary_window)
        self.summary_text.pack()
        self.update_summary()

    def update_summary(self):
        # Update summary text
        summary = self.db.get_summary()
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)

    def view_analytics(self):
        # Create a new window for analytics
        self.analytics_window = tk.Toplevel(self.root)
        self.analytics_window.title("Analytics")
        self.create_analytics_widgets()

    def create_analytics_widgets(self):
        # Create widgets for displaying analytics
        self.analytics_text = tk.Text(self.analytics_window)
        self.analytics_text.pack()
        self.update_analytics()

    def update_analytics(self):
        # Update analytics text
        analytics = Analytics(self.db).get_analytics()
        self.analytics_text.delete(1.0, tk.END)
        self.analytics_text.insert(tk.END, analytics)

if __name__ == "__main__":
    gui = GUI(Database())
    gui.mainloop()