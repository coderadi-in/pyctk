'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.title("Place Manager")
root.geometry("600x400")

# | A Label
CTkLabel(
    root, text="Hello World",
    fg_color="blue", text_color="white"
).place(
    x=5, y=50
)

# ! Run the UI 
root.mainloop()