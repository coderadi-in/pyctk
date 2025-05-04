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

# | CTkFont
font_a = CTkFont(
    family="Arial",
    size=20,
    weight="bold"
)

CTkLabel(
    root, text="Hello", font=font_a
).pack()
CTkLabel(
    root, text="Hello", font=font_a
).pack()
CTkLabel(
    root, text="Hello", font=font_a
).pack()

CTkButton(
    root, text="Click",
    font=font_a,
    width=font_a.measure("Click") + 20
).pack()

# add padding of 10px each side

# ! Run the UI
root.mainloop()