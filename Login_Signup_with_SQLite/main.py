import tkinter as tk
import tkinter.ttk as ttk

# create the main Tkinter window
window = tk.Tk()

# -------------------------

def show_login():
    notebook.select(login_tab)


def show_register():
    notebook.select(register_tab)

def login_to_system():
    pass

def submit_registration():
    pass

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

login_btn = ttk.Button(login_tab, text="LOGIN", command=login_to_system)
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
