'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *
import tool

# ! The Root Window
root = CTk(fg_color="#0E0E10")
root.title("Language Translator")
root.geometry("600x400")

# * Function to show text
def ui_translate():
    text = inp.get()
    output = tool.translate(text)

    # delete output entry texts
    out_text.delete(0, END)
    pro_text.delete(0, END)

    # insert new text
    out_text.insert(0, output.output)
    pro_text.insert(0, output.pronunciation)

# | Text Input
inp = CTkEntry(
    root, text_color="#F3F4F6", fg_color="#3F3F46", border_color="#27272A", border_width=2, placeholder_text="Enter text",
    placeholder_text_color="#A1A1AA", width=200
)
inp.pack(side='top', pady=5)

# | Button
btn = CTkButton(
    root, text="Translate", fg_color="#4C8EFF", text_color="#F3F4F6", hover=True, hover_color="#3F3F46", cursor="hand2", width=200, command=ui_translate
)
btn.pack(side="top", pady=5)

# | Output Text
out_text = CTkEntry(
    root, text_color="#F3F4F6", fg_color="#3F3F46", border_color="#27272A", border_width=2, width=200
)
out_text.pack(side='top', pady=5)

# | Pronunciation Text
pro_text = CTkEntry(
    root, text_color="#F3F4F6", fg_color="#3F3F46", border_color="#27272A", border_width=2, width=200
)
pro_text.pack(side='top', pady=5)

# ! Run the App
root.mainloop()