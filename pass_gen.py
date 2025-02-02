import tkinter as tk
from tkinter import ttk
import random
import string
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')
        
        # Password display frame
        self.password_frame = tk.Frame(root, bg='white', pady=20)
        self.password_frame.pack(fill='x', padx=20, pady=(20,0))
        
        self.password_var = tk.StringVar(value="password")
        self.password_label = tk.Entry(
            self.password_frame, 
            textvariable=self.password_var,
            font=('Courier', 14),
            justify='center',
            bd=0,
            readonlybackground='white',
            state='readonly'
        )
        self.password_label.pack(fill='x', padx=10)
        
        # Main options frame
        self.options_frame = tk.Frame(root, bg='white', pady=20)
        self.options_frame.pack(fill='x', padx=20, pady=20)
        
        # Password Length section
        tk.Label(
            self.options_frame,
            text="Password Length",
            font=('Arial', 10, 'bold'),
            bg='white'
        ).pack(anchor='w', padx=20)
        
        # Length control frame
        self.length_frame = tk.Frame(self.options_frame, bg='white')
        self.length_frame.pack(fill='x', padx=20, pady=(0,10))
        
        # Spinbox for password length
        self.length_var = tk.StringVar(value="12")
        self.length_spinbox = ttk.Spinbox(
            self.length_frame,
            from_=1,
            to=50,
            textvariable=self.length_var,
            width=5,
            command=self.on_length_change
        )
        self.length_spinbox.pack(side='left', pady=5)
        
        # Slider for password length
        self.length_slider = ttk.Scale(
            self.length_frame,
            from_=1,
            to=50,
            orient='horizontal',
            variable=self.length_var,
            command=self.on_slider_change
        )
        self.length_slider.pack(side='left', fill='x', expand=True, padx=(10,0))
        
        # Character options
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        # Options checkboxes
        options = [
            ("Uppercase", self.uppercase_var),
            ("Lowercase", self.lowercase_var),
            ("Numbers", self.numbers_var),
            ("Symbols", self.symbols_var)
        ]
        
        for text, var in options:
            cb = ttk.Checkbutton(
                self.options_frame,
                text=text,
                variable=var,
                command=self.generate_password
            )
            cb.pack(anchor='w', padx=20, pady=2)
        
        # Generate button
        self.generate_btn = tk.Button(
            root,
            text="Generate Password",
            font=('Arial', 12),
            bg='#e91e63',
            fg='white',
            relief='flat',
            command=self.generate_password,
            pady=10
        )
        self.generate_btn.pack(fill='x', padx=20, pady=20)
        
        # Copy button
        self.copy_btn = tk.Button(
            root,
            text="Copy Password",
            font=('Arial', 12),
            bg='#2196f3',
            fg='white',
            relief='flat',
            command=self.copy_password,
            pady=10
        )
        self.copy_btn.pack(fill='x', padx=20)
        
        # Generate initial password
        self.generate_password()
        
    def on_length_change(self):
        try:
            length = int(self.length_var.get())
            if 1 <= length <= 50:
                self.generate_password()
            else:
                self.length_var.set("12")
        except ValueError:
            self.length_var.set("12")
            
    def on_slider_change(self, value):
        self.length_var.set(int(float(value)))
        self.generate_password()
        
    def generate_password(self):
        # Get the selected character types
        chars = ""
        if self.uppercase_var.get():
            chars += string.ascii_uppercase
        if self.lowercase_var.get():
            chars += string.ascii_lowercase
        if self.numbers_var.get():
            chars += string.digits
        if self.symbols_var.get():
            chars += string.punctuation
            
        # Check if at least one character type is selected
        if not chars:
            messagebox.showwarning(
                "Warning",
                "Please select at least one character type!"
            )
            self.lowercase_var.set(True)
            chars = string.ascii_lowercase
            
        try:
            length = int(self.length_var.get())
            # Generate password
            password = ''.join(random.choice(chars) for _ in range(length))
            self.password_var.set(password)
        except ValueError:
            self.length_var.set("12")
            self.generate_password()
            
    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())
        messagebox.showinfo("Success", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()