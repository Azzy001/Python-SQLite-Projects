import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3
import random
import time

# create tkinter window
window = tk.Tk()


def submit_sale():   
    try:
        # connect to SQLite database
        conn = sqlite3.connect("vehicle_ms/vehicle_sale_db")
        cursor = conn.cursor()
        
        # check if the table exists, if not, create it
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customer_tb (
            invoice_id TEXT PRIMARY KEY,
            customer_name TEXT,
            customer_number TEXT,
            customer_email TEXT,
            customer_address TEXT,
            customer_postcode TEXT
        );
        
        CREATE TABLE IF NOT EXISTS vehicle_tb (
            invoice_id TEXT PRIMARY KEY,
            vehicle_brand TEXT,
            vehicle_make TEXT,
            vehicle_colour TEXT,
            vehicle_milage TEXT,
            vehicle_cost TEXT
        );
        """
        cursor.executescript(create_table_query)
        
        invoice_id = random.randint(00000, 99999)
    
        # get values from the entry widgets
        customer_name = customer_name_entry.get()
        customer_number = customer_number_entry.get()
        customer_email = customer_email_entry.get()
        customer_address = customer_address_entry.get()
        customer_postcode = customer_postcode_entry.get()
        
        vehicle_brand = vehicle_brand_entry.get()
        vehicle_make = vehicle_make_entry.get()
        vehicle_colour = vehicle_colour_entry.get()
        vehicle_milage = vehicle_milage_entry.get()
        vehicle_cost = vehicle_cost_entry.get()
        
        insert_customer_query = """
        INSERT INTO customer_tb (
            invoice_id,
            customer_name, 
            customer_number, 
            customer_email,
            customer_address, 
            customer_postcode
        ) VALUES (?, ?, ?, ?, ?, ?)
        """
        
        cursor.execute(insert_customer_query, (
            invoice_id,
            customer_name, 
            customer_number, 
            customer_email, 
            customer_address, 
            customer_postcode
        ))
        
        insert_vehicle_query = """ 
        INSERT INTO vehicle_tb (
            invoice_id,
            vehicle_brand,
            vehicle_make, 
            vehicle_colour, 
            vehicle_milage, 
            vehicle_cost
            ) VALUES (?, ?, ?, ?, ?, ?)
        """
            
        cursor.execute(insert_vehicle_query, (
            invoice_id, 
            vehicle_brand, 
            vehicle_make, 
            vehicle_colour,
            vehicle_milage, 
            vehicle_cost
            ))
        
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'Vehicle Sales added successfully.')
        
    except Exception as e:
        # display an error message if something goes wrong
        messagebox.showerror("Error", f"An error has occurred: {str(e)}")

# ----------------------------------------

def clear_sale_entry():
    customer_name_entry.delete(0, tk.END)
    customer_number_entry.delete(0, tk.END)
    customer_email_entry.delete(0, tk.END)
    customer_address_entry.delete(0, tk.END)
    customer_postcode_entry.delete(0, tk.END)

    vehicle_brand_entry.delete(0, tk.END)
    vehicle_make_entry.delete(0, tk.END)
    vehicle_colour_entry.delete(0, tk.END)
    vehicle_milage_entry.delete(0, tk.END)
    vehicle_cost_entry.delete(0, tk.END)

# ----------------------------------------

# frame 1 
left_frame = ttk.Frame(window)
left_frame.pack(side="left", padx=10, pady=10)

customer_name_label = ttk.Label(left_frame, text="Customer name:")
customer_name_label.grid(row=1, column=0, padx=10, pady=10)
customer_name_entry = ttk.Entry(left_frame, width=30)
customer_name_entry.grid(row=1, column=1, padx=10, pady=10)

customer_number_label = ttk.Label(left_frame, text="Customer number:")
customer_number_label.grid(row=2, column=0, padx=10, pady=10)
customer_number_entry = ttk.Entry(left_frame, width=30)
customer_number_entry.grid(row=2, column=1, padx=10, pady=10)

customer_email_label = ttk.Label(left_frame, text="Customer email:")
customer_email_label.grid(row=3, column=0, padx=10, pady=10)
customer_email_entry = ttk.Entry(left_frame, width=30)
customer_email_entry.grid(row=3, column=1, padx=10, pady=10)

customer_address_label = ttk.Label(left_frame, text="Customer address:")
customer_address_label.grid(row=4, column=0, padx=10, pady=10)
customer_address_entry = ttk.Entry(left_frame, width=30)
customer_address_entry.grid(row=4, column=1, padx=10, pady=10)

customer_postcode_label = ttk.Label(left_frame, text="Customer postcode:")
customer_postcode_label.grid(row=5, column=0, padx=10, pady=10)
customer_postcode_entry = ttk.Entry(left_frame, width=30)
customer_postcode_entry.grid(row=5, column=1, padx=10, pady=10)

# ----------------------------------------

# frame 2
centre_frame = tk.Frame(window)
centre_frame.pack(side="left", padx=10, pady=10)

vehicle_brand_label = ttk.Label(centre_frame, text="Vehicle brand:")
vehicle_brand_label.grid(row=1, column=0, padx=10, pady=10)
vehicle_brand_entry = ttk.Entry(centre_frame, width=30)
vehicle_brand_entry.grid(row=1, column=1, padx=10, pady=10)

vehicle_make_label = ttk.Label(centre_frame, text="Vehicle brand:")
vehicle_make_label.grid(row=2, column=0, padx=10, pady=10)
vehicle_make_entry = ttk.Entry(centre_frame, width=30)
vehicle_make_entry.grid(row=2, column=1, padx=10, pady=10)

vehicle_colour_label = ttk.Label(centre_frame, text="Vehicle color:")
vehicle_colour_label.grid(row=3, column=0, padx=10, pady=10)
vehicle_colour_entry = ttk.Entry(centre_frame, width=30)
vehicle_colour_entry.grid(row=3, column=1, padx=10, pady=10)

vehicle_milage_label = ttk.Label(centre_frame, text="Vehicle milage:")
vehicle_milage_label.grid(row=4, column=0, padx=10, pady=10)
vehicle_milage_entry = ttk.Entry(centre_frame, width=30)
vehicle_milage_entry.grid(row=4, column=1, padx=10, pady=10)

vehicle_cost_label = ttk.Label(centre_frame, text="Vehicle cost:")
vehicle_cost_label.grid(row=5, column=0, padx=10, pady=10)
vehicle_cost_entry = ttk.Entry(centre_frame, width=30)
vehicle_cost_entry.grid(row=5, column=1, padx=10, pady=10)

# ----------------------------------------

# frame 3
right_frame = tk.Frame(window)
right_frame.pack(side="right", padx=10, pady=10)

receipt_text = tk.Text(right_frame, height=20, width=35, state=tk.DISABLED)
receipt_text.grid(row=0, column=0, padx=10, pady=10)

# ----------------------------------------

# frame 4
bottom_frame = tk.Frame(window)
bottom_frame.place(x=10, y=310)

add_sale = tk.Button(bottom_frame, width=20, text="Submit Sale", height=2, command=submit_sale)
add_sale.grid(row=0, column=0, padx=10, pady=10)

clear_sale = tk.Button(bottom_frame, width=20, text="Clear Sale", height=2, command=clear_sale_entry)
clear_sale.grid(row=0, column=1, padx=10, pady=10)

btn3 = tk.Button(bottom_frame, width=20, text="", height=2)
btn3.grid(row=0, column=2, padx=10, pady=10)

btn4 = tk.Button(bottom_frame, width=20, text="", height=2)
btn4.grid(row=0, column=3, padx=10, pady=10)

# ----------------------------------------

# create window properties
window.attributes("-topmost", True)
window.geometry("1010x400")
window.resizable(0, 0)
window.title("Arsalan's Vehicle Management System")
# window.configure(background="#8eacf3")
window.mainloop()