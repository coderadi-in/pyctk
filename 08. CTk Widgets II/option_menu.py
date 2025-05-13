'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.geometry("600x400")
root.title("Option Menu | PyCODE")

# | Option Menu
CTkOptionMenu(
    root, values=[
        "option 1",
        "option 2",
        "option 3"
    ]
).pack()

# | Combo Box
CTkComboBox(
    root, values=[
        "option 1",
        "option 2",
        "option 3"
    ]
).pack()

# ! Run the UI
root.mainloop()