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

# ! Run the UI
root.mainloop()