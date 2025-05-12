'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.geometry("600x400")
root.title("CTk Segmented Button")

# | Frame : Python 
f1 = CTkFrame(root)
label1 = CTkLabel(f1, text="Python")
label1.pack(pady=20)
entry1 = CTkEntry(f1, placeholder_text="Python")
entry1.pack(pady=20)

# | Frame : JavaScript
f2 = CTkFrame(root)
label2 = CTkLabel(f2, text="JavaScript")
label2.pack(pady=20)
entry2 = CTkEntry(f2, placeholder_text="JavaScript")
entry2.pack(pady=20)

# | Frame : C/C++
f3 = CTkFrame(root)
label3 = CTkLabel(f3, text="C/C++")
label3.pack(pady=20)
entry3 = CTkEntry(f3, placeholder_text="C/C++")
entry3.pack(pady=20)

# * Button Callback
def callback(event=None):
    value = button.get()
    # Hide all frames first
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()

    # Show the selected frame
    if value == 'Python':
        f1.pack(pady=20)
    elif value == 'JavaScript':
        f2.pack(pady=20)
    elif value == 'C/C++':
        f3.pack(pady=20)

button = CTkSegmentedButton(
    root,
    values=[
        "Python",
        "JavaScript",
        "C/C++"
    ], command=callback
)
button.pack(pady=20)
button.set("Python")
callback()  # Initialize the UI with the default selection

# ! Run the UI
root.mainloop()