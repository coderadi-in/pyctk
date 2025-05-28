'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.title("Textbox")
root.geometry("600x400")

def print_text():
    print(text.get(1.0, END)) # Get text from index 1.0 (starting) to END
    text.insert(END, "\nText")

# | Entry - One line of text.
# | Textbox - Multiple lines of texts.

text = CTkTextbox(root)
text.pack(
    expand=True, fill=BOTH,
    padx=5, pady=5
)

CTkButton(
    root, text="Click",
    command=print_text
).pack(
    expand=True, fill=BOTH,
    padx=5, pady=(0, 5)
)

# ! Run the UI
root.mainloop()

# | A Multiline Entry
# | Created using CTkTextbox()
# | .get() is used to get text of it.
# | .insert() is used to insert text in it.

# & Try to build a text editor