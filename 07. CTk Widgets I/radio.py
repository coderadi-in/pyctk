'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.title("Radio Button")
root.geometry("600x400")

# | Variable
var = IntVar()

# | Radio button
r1 = CTkRadioButton(
    root, text='Python',
    variable=var, value=0
)
r1.pack()

r2 = CTkRadioButton(
    root, text='JavaScript',
    variable=var, value=1
)
r2.pack()

r3 = CTkRadioButton(
    root, text='C',
    variable=var, value=2
)
r3.pack()

r4 = CTkRadioButton(
    root, text='Go',
    variable=var, value=3
)
r4.pack()

# ! Run the UI
root.mainloop()