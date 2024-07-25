import tkinter as tk
from tkinter import messagebox

def add_colour():
    new_colour = input("Enter new colour: ")
    listbox.insert(tk.END, new_colour)
    colours.append(new_colour)

def remove_colour():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        colours.pop(selected_index)
    except IndexError:
        messagebox.showerror("Error", "Select a colour to remove")

def apply_colour():
    try:
        selected_index = listbox.curselection()[0]
        selected_colour = colours[selected_index]
        root.config(bg=selected_colour)
    except IndexError:
        messagebox.showerror("Error", "Select a colour to apply")

root = tk.Tk()
root.title("Colour Picker")

colours = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]

listbox = tk.Listbox(root)
for colour in colours:
    listbox.insert(tk.END, colour)
listbox.pack(padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

add_button = tk.Button(button_frame, text="Add Colour", command=add_colour)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(button_frame, text="Remove Colour", command=remove_colour)
remove_button.pack(side=tk.LEFT, padx=5)

apply_button = tk.Button(button_frame, text="Apply Colour", command=apply_colour)
apply_button.pack(side=tk.LEFT, padx=5)

root.mainloop()