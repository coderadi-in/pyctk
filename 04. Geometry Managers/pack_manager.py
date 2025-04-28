'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.geometry("600x400")
root.title("Pack Manager")

CTkLabel(
    root, text="Hello World",
    fg_color="black", 
    text_color="white"
).pack(
    side="left",
    fill="x",
    expand=True,
    padx=5, pady=5,
    ipadx=5, ipady=5
)

# ! Run the App
root.mainloop()