'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *
from PIL import Image

# ! The Root Window
root = CTk()
root.geometry("600x400")
root.title("Utilities")

# | CTkImage
img = CTkImage(
    light_image=Image.open("06. Utilities/img.jpeg"), size=(
        250, 250
    )
)

CTkLabel(
    root, image=img, text=""
).pack()

# ! Run the UI
root.mainloop()