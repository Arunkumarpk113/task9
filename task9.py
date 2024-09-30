#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    
    if not name or not email or not password:
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showinfo("Registration", f"Registration successful!\nName: {name}\nEmail: {email}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x200")

# Create labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)

entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)

entry_email = tk.Entry(root)
entry_email.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=5)

# Create a Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
