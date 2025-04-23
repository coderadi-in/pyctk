'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.title("Basic Widgets")
root.geometry("600x400")

# | Label
label = CTkLabel(
    root, text="Hello world", text_color="#0000ff",
    fg_color="#00ff00",
    bg_color="#000000",
    corner_radius=10,
    font=("Arial", 20, "bold")
)
label.pack()

# | Entry
entry = CTkEntry(
    root, 
    width=200,
    height=40,
    corner_radius=5,
    fg_color="#282828",
    placeholder_text="Enter your name",
    text_color="#EDEDED",
    placeholder_text_color="#505050"
)
entry.pack()

# | Insert Method
entry.insert(0, "Hello")

# | Get Method
print(entry.get())

# | Delete Method
entry.delete(0, END)

# ! Run the UI
root.mainloop()