import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-"
    password = ''.join(random.sample(characters, length))
    generated_password_var.set(password)

def copy_password():
    password = generated_password_var.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.geometry("250x200")
root.title("Password Generator")

length_label = tk.Label(root, text="Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack()

generated_password_var = tk.StringVar()
generated_password_label = tk.Label(root, textvariable=generated_password_var)
generated_password_label.pack()

copy_button = tk.Button(root, text="Copy", command=copy_password)
copy_button.pack()

root.mainloop()
