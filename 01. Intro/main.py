'''PyCODE | @_py.code'''

# $ pip install customtkinter --upgrade

# | Window

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk() # Main Window

# | Appearance Mode (Theme)
set_appearance_mode('system')

# | Sizing
geomtry = "600x400+100+100"
# geomtry = "{width}x{height}"
root.geometry(geomtry)

# | Title
root.title("My App")

# | Icon
root.iconbitmap('icon.ico')

# | State
root.state('zoomed')

# | Color
root.configure(fg_color='#FF0000')

# ! Run the UI
root.mainloop()

# | source code at github