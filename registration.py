import customtkinter as ctk
from tkinter import messagebox
import sqlite3

# Initialize the main window
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Registration Form")
root.geometry("700x800")
root.resizable(True, True)

# Variables
fullname = ctk.StringVar()
address = ctk.StringVar()
username = ctk.StringVar()
email = ctk.StringVar()
phoneno = ctk.IntVar()
age = ctk.IntVar()
password = ctk.StringVar()
password1 = ctk.StringVar()

# Background Frame
frame = ctk.CTkFrame(root, width=500, height=650, fg_color=("#ffffff", "#e3f2fd"))
frame.pack(fill="both", expand=True)

# Title Label
title_label = ctk.CTkLabel(frame, text="Create an Account", font=("Arial", 24, "bold"), text_color="#0078D7")
title_label.pack(pady=20)

# Function to create labeled entry fields in a box-like structure
def create_input_box(parent, label_text, variable, show_text=""):
    box_frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=10, border_width=1, border_color="#b0bec5")
    box_frame.pack(pady=5, padx=20, fill="x")

    label = ctk.CTkLabel(box_frame, text=label_text, font=("Arial", 14, "bold"), text_color="#0078D7", anchor="w")
    label.pack(padx=10, pady=2, anchor="w")

    entry = ctk.CTkEntry(box_frame, textvariable=variable, placeholder_text=label_text, width=300, height=30, show=show_text, corner_radius=10)
    entry.pack(padx=10, pady=5, fill="x")

# Input Fields
create_input_box(frame, "Full Name", fullname)
create_input_box(frame, "Address", address)
create_input_box(frame, "Username", username)
create_input_box(frame, "Email", email)
create_input_box(frame, "Phone Number", phoneno)
create_input_box(frame, "Age", age)
create_input_box(frame, "Password", password, show_text="*")
create_input_box(frame, "Confirm Password", password1, show_text="*")

# Registration Function
def register():
    if not fullname.get() or not address.get() or not username.get() or not email.get() or not phoneno.get() or not age.get() or not password.get() or not password1.get():
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if password.get() != password1.get():
        messagebox.showerror("Error", "Passwords do not match!")
        return
    
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS admin_registration (id INTEGER PRIMARY KEY AUTOINCREMENT, fullname TEXT, address TEXT, username TEXT UNIQUE, email TEXT, phoneno INTEGER, age INTEGER, password TEXT)")
        
        try:
            c.execute("INSERT INTO admin_registration (fullname, address, username, email, phoneno, age, password) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                      (fullname.get(), address.get(), username.get(), email.get(), phoneno.get(), age.get(), password.get()))
            db.commit()
            messagebox.showinfo("Success", "Registration Successful!")
            root.destroy()
            import login
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

# Register Button
register_button = ctk.CTkButton(frame, text="Register", command=register, width=300, height=40, fg_color="#0078D7", hover_color="#005BB5", corner_radius=10)
register_button.pack(pady=10)

# Back to Login Function
def back_to_login():
    root.destroy()
    import login

# Back Button
back_button = ctk.CTkButton(frame, text="Back to Login", command=back_to_login, width=300, height=40, fg_color="#E53935", hover_color="#C62828", corner_radius=10)
back_button.pack(pady=10)

root.mainloop()
