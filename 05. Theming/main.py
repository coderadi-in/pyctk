'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
set_default_color_theme('05. Theming/design.json')
set_appearance_mode('dark')
root.geometry("600x400")
root.title("Theme")

# | A Label
CTkLabel(
    root, text="Hello world"
).pack()

# ! Run the UI 
root.mainloop()