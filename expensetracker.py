import tkinter as tk
from gui import GUI
from database import Database

def main():
    db = Database()
    gui = GUI(db)
    gui.root.mainloop()

if __name__ == "__main__":
    main()