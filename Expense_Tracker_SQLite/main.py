import random
import time
import sqlite3
from rich.console import Console
from rich.table import Table



# --------------------

def create_table():
    """Function initialises and returns a new expense tracker table with predicted columns"""
    
    print("\n\n")
    table = Table(title="Expense Tracker")
    table.add_column("Item ID", style="cyan")
    table.add_column("Item name", style="cyan")
    table.add_column("Item category", style="cyan")
    table.add_column("Item cost (per)", style="cyan")
    table.add_column("quantity", style="cyan")
    table.add_column("Total cost", style="cyan")
    table.add_column("Retailer name", style="cyan")
    table.add_column("Date of purchase", style="cyan")
    
    return table

# --------------------

def add_items_to_table():
    pass

# --------------------

def display_table(table):
    """This function prints the formatted expense tracker table to the console"""
    
    console = Console()
    console.print(table)
    print("\n")
    
# --------------------

# connect to SQLite database
conn = sqlite3.connect("expense_tracker_db")

# call the function
expense_table = create_table()
display_table(expense_table)