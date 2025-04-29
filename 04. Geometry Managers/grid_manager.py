'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.geometry("600x400")
root.title("Grid")

# | Label
CTkLabel(
    root, text="Hello World",
    fg_color="#000000",
    text_color="#FFFFFF"
).grid(
    row=0, column=0,
    rowspan=1, columnspan=1,
    padx=5, pady=5, 
    ipadx=5, ipady=5
)

CTkLabel(
    root, text="Hello World",
    fg_color="#000000",
    text_color="#FFFFFF"
).grid(
    row=0, column=1,
    rowspan=1, columnspan=1,
    padx=5, pady=5, 
    ipadx=5, ipady=5
)

CTkLabel(
    root, text="Hello World",
    fg_color="#000000",
    text_color="#FFFFFF"
).grid(
    row=1, column=0,
    rowspan=1, columnspan=2,
    sticky="nsew",
    padx=5, pady=5, 
    ipadx=5, ipady=5
)

# ! Run the UI
root.mainloop()