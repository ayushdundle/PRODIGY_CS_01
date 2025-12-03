import tkinter as tk
from tkinter import ttk, messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def perform_action():
    message = entry_message.get()
    shift = entry_shift.get()

    if not shift.isdigit():
        messagebox.showerror("Error", "Shift value must be a number!")
        return

    shift = int(shift)

    if selected_option.get() == "Encrypt":
        output = encrypt(message, shift)
    else:
        output = decrypt(message, shift)

    output_box.config(state="normal")
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, output)
    output_box.config(state="disabled")

root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("420x330")
root.resizable(False, False)

title_label = tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

label_message = tk.Label(root, text="Enter Message:", font=("Arial", 12))
label_message.pack()
entry_message = tk.Entry(root, width=40, font=("Arial", 12))
entry_message.pack(pady=5)

label_shift = tk.Label(root, text="Enter Shift Value:", font=("Arial", 12))
label_shift.pack()
entry_shift = tk.Entry(root, width=10, font=("Arial", 12))
entry_shift.pack(pady=5)

selected_option = tk.StringVar(value="Encrypt")
option_menu = ttk.Combobox(root, textvariable=selected_option, values=["Encrypt", "Decrypt"], state="readonly")
option_menu.pack(pady=10)

btn = tk.Button(root, text="Run Cipher", font=("Arial", 12, "bold"), command=perform_action)
btn.pack(pady=10)

label_output = tk.Label(root, text="Output:", font=("Arial", 12))
label_output.pack()

output_box = tk.Text(root, height=4, width=40, font=("Arial", 12))
output_box.pack()
output_box.config(state="disabled")

root.mainloop()
