'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.title("CTk Widgets I")
root.geometry("600x400")

def hello():
    print("Hello")

# | Checkbox
c1 = CTkCheckBox(
    root, text="option 1", state="normal", command=hello,
    checkbox_height=50, checkbox_width=50
)
c1.pack()

# | Basic Methods
print(c1.get())

# ! Run the UI
root.mainloop()