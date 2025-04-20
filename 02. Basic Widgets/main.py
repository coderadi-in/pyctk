'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.title("Basic Widgets")
root.geometry("600x400")

# | Label
label = CTkLabel(
    root, text="Hello world"
)
label.pack()

# ! Run the UI
root.mainloop()