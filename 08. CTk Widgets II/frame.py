'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.geometry("600x400")
root.title("Frame")

# | Some Widgets
label = CTkLabel(
    root, text="Hello World"
)
label.pack()

btn = CTkButton(
    root, text="Click",
    command=lambda: [
        frame.pack_forget() #1
    ]
)
btn.pack()

# | frame
frame = CTkFrame(
    root, fg_color="#1A1A1D"
)
frame.pack(
    padx=10, pady=10,
    ipadx=10, ipady=10
)

# | Some Widgets
CTkLabel(
    frame, text="Hello World"
).pack()

CTkButton(
    frame, text="Click",
    command=lambda: [
       label.pack_forget(),
       btn.pack_forget()
    ]
).pack()

# ! Run the UI
root.mainloop()