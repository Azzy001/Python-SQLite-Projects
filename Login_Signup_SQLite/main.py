import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from tkinter import messagebox
import bcrypt
import uuid

# create the main Tkinter window
window = tk.Tk()

# -------------------------

def show_login():
    notebook.select(login_tab)


def show_register():
    notebook.select(register_tab)


# -------------------------

def submit_login():
    # connect to SQLite database
    with sqlite3.connect("customer_db") as conn:
        cursor = conn.cursor()
    
    # get values from the entry widget
    entered_email = login_email_entry.get()
    entered_password = login_password_entry.get()
    
    # query the database to check for matching email and password
    query = """
    SELECT customer_id, customer_password FROM customer_tb
    WHERE customer_email = ?
    """
        
    cursor.execute(query, (entered_email,))
    result = cursor.fetchone()
    
    if result:
        # authenticate successful, proceed with the desired action
        stored_hashed_password = result[1]
        
        # check if the entered password matches the stored hashed password
        if bcrypt.checkpw(entered_password.encode("utf-8"), stored_hashed_password.encode("utf-8")):
            messagebox.showinfo("Success", "Login successful.")
            open_main_window()
                
        else:
            # authentication failed, show error message
            messagebox.showerror("Error", "Invalid email or password. Please try again.")
    
    else:
        # user not found, show error message
        print("Entered Email:", entered_email)
        print("Query:", query)
        print("User does not exist.")
        # user not found, show error message
        messagebox.showerror("Error", "User does not exist.")
    
# -------------------------

def submit_registration():
    try:
        # connect to SQLite database
        with sqlite3.connect("customer_db") as conn:
            cursor = conn.cursor()
        
        # check if table exists, if not, create it
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customer_tb (
          customer_id TEXT PRIMARY KEY,
          customer_name,
          customer_email,
          customer_password  
        );
        """
        cursor.execute(create_table_query)
        
        # use a more robust customer id
        customer_id = str(uuid.uuid4())
        
        # get values from the entry widgets
        customer_name = register_username_entry.get()
        customer_email = register_email_entry.get()
        customer_password = register_password_entry.get()
        
        if register_password_entry.get() == register_password_confirm_entry.get():
            hashed_password = bcrypt.hashpw(customer_password.encode("utf-8"), bcrypt.gensalt())
            insert_customer_query = """
            INSERT INTO customer_tb (
                customer_id,
                customer_name,
                customer_email,
                customer_password
            ) VALUES (?, ?, ?, ?)
            """
            
            cursor.execute(insert_customer_query, (
                customer_id,
                customer_name,
                customer_email,
                hashed_password.decode('utf-8')
            ))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Customer successfully registered.")
        
        else:
            messagebox.showerror("Error", "Both password's do not match.")    
                
    # display an error message if something goes wrong
    except Exception as e:
        messagebox.showerror("Error", f"An error has occurred: {str(e)}")
        

def open_main_window():
    # save the current window's geometry
    current_geometry = window.geometry()
    
    # close the current window
    window.destroy()
    
    # create and configure the new window with the same geometry
    main_window = tk.Tk()
    main_window.geometry(current_geometry)
    
    # run the maiun loop for the new window
    main_window.mainloop()

# -------------------------

# create a notebook widget
notebook = ttk.Notebook(window)

# create tabs with associated frames
login_tab = ttk.Frame(notebook)
register_tab = ttk.Frame(notebook)

# add tabs to the notebook
notebook.add(login_tab, text="Login")
notebook.add(register_tab, text="Register")

# configure ttk.Style to customize the tabs
style = ttk.Style()
style.configure("TNotebook", tabposition="n")  # Position tabs at the top

style.configure(
    "TNotebook.Tab",
    padding=[50, 5],  # Adjust padding for a larger tab size
    font=("Arial", 13),  # Adjust font size for the tab text
)

# -------------------------

# login widgets
empty_label = ttk.Label(login_tab, text="")
empty_label.grid(row=0, column=0, padx=40, pady=10)

login_email_label = ttk.Label(login_tab, text="Enter email address:")
login_email_label.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

login_email_entry = ttk.Entry(login_tab, width=30)
login_email_entry.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)

login_password_label = ttk.Label(login_tab, text="Enter password:")
login_password_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

login_password_entry = ttk.Entry(login_tab, width=30)
login_password_entry.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)

login_btn = ttk.Button(login_tab, text="LOGIN", command=submit_login)
login_btn.grid(row=3, column=1, columnspan=1, pady=10, sticky="ew")


# -------------------------

# register widgets
empty_label = ttk.Label(register_tab, text="")
empty_label.grid(row=0, column=0, padx=40, pady=10)

register_username_label = ttk.Label(register_tab, text="Enter Full name:")
register_username_label.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

register_username_entry = ttk.Entry(register_tab, width=30)
register_username_entry.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)


register_email_label = ttk.Label(register_tab, text="Enter email address:")
register_email_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

register_email_entry = ttk.Entry(register_tab, width=30)
register_email_entry.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)


register_password_label = ttk.Label(register_tab, text="Choose a password:")
register_password_label.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

register_password_entry = ttk.Entry(register_tab, width=30)
register_password_entry.grid(row=3, column=2, padx=10, pady=10, sticky=tk.W)


register_password_confirm_label = ttk.Label(register_tab, text="Confirm password:")
register_password_confirm_label.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

register_password_confirm_entry = ttk.Entry(register_tab, width=30)
register_password_confirm_entry.grid(row=4, column=2, padx=10, pady=10, sticky=tk.W)

register_btn = ttk.Button(register_tab, text="REGISTER", command=submit_registration)
register_btn.grid(row=5, column=1, columnspan=1, pady=10, sticky="ew")

# -------------------------

# bind a function to the tab change event
notebook.bind("<<NotebookTabChanged>>")

# pack the notebook at the top center underneath the title
notebook.grid(row=1, column=0, columnspan=2, sticky="nsew")

# configure grid row and column weights to make the frame expand
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)


# window configurations
window.title("Arsalan's Login System")
window.configure(background="#3399ff")
window.geometry("500x550")
window.resizable(0, 0)
window.mainloop()