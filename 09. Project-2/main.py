'''PyCODE | @_py.code'''

# ? Importing Libraries
from customtkinter import *

# ! The Root Window
root = CTk()
root.geometry("400x600")
root.title("Calculator")

# * Utilities
lf = CTkFont("Arial", 40)
sf = CTkFont("Arial", 20)

# * Colors
blue = "#2483ff"
red = "#cc2f2f"
green = "#00ff00"
hover = "#eaebc5"
text_color = "#1a1a1d"

# * Functions
def click(event):
    widget = event.widget
    button = widget.master
    text = button.cget("text")
    display.insert(END, text)

def clear(event):
    display.delete(0, END)

def calculate(event):
    query = display.get()
    try:
        res = eval(query)
    except Exception as e:
        res = "Error"
        print(e)

    clear(None)
    display.insert(0, res)

def backspace(event):
    text = display.get()
    if len(text) > 0:
        newtext = text[:-1]
        clear(None)
        display.insert(0, newtext)

# | Display
display = CTkEntry(
    root, width=380, height=70,
    font=lf
)
display.grid(
    row=0, column=0, padx=10, pady=10
)

# | Keypad
nums = CTkFrame(
    root, width=380, height=490,
)
nums.grid(
    row=1, column=0, padx=10, pady=10
)

# * Numerical Buttons
b1 = CTkButton(
    nums, text="1", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b1.grid(
    row=0, column=0, padx=5, pady=5
)
b1.bind("<Button-1>", click)

b2 = CTkButton(
    nums, text="2", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b2.grid(
    row=0, column=1, padx=5, pady=5
)
b2.bind("<Button-1>", click)

b3 = CTkButton(
    nums, text="3", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b3.grid(
    row=0, column=2, padx=5, pady=5
)
b3.bind("<Button-1>", click)

b4 = CTkButton(
    nums, text="4", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b4.grid(
    row=1, column=0, padx=5, pady=5
)
b4.bind("<Button-1>", click)

b5 = CTkButton(
    nums, text="5", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b5.grid(
    row=1, column=1, padx=5, pady=5
)
b5.bind("<Button-1>", click)

b6 = CTkButton(
    nums, text="6", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b6.grid(
    row=1, column=2, padx=5, pady=5
)
b6.bind("<Button-1>", click)

b7 = CTkButton(
    nums, text="7", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b7.grid(
    row=2, column=0, padx=5, pady=5
)
b7.bind("<Button-1>", click)

b8 = CTkButton(
    nums, text="8", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b8.grid(
    row=2, column=1, padx=5, pady=5
)
b8.bind("<Button-1>", click)

b9 = CTkButton(
    nums, text="9", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b9.grid(
    row=2, column=2, padx=5, pady=5
)
b9.bind("<Button-1>", click)

b0 = CTkButton(
    nums, text="0", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b0.grid(
    row=3, column=1, padx=5, pady=5
)
b0.bind("<Button-1>", click)

b_dot = CTkButton(
    nums, text=".", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b_dot.grid(
    row=3, column=0, padx=5, pady=5
)
b_dot.bind("<Button-1>", click)

# * Operator Buttons
b_plus = CTkButton(
    nums, text="+", width=85, height=85, font=sf, fg_color=green, hover_color=hover, text_color=text_color
)
b_plus.grid(
    row=0, column=3, padx=5, pady=5
)
b_plus.bind("<Button-1>", click)

b_minus = CTkButton(
    nums, text="-", width=85, height=85, font=sf, fg_color=green, hover_color=hover, text_color=text_color
)
b_minus.grid(
    row=1, column=3, padx=5, pady=5
)
b_minus.bind("<Button-1>", click)

b_multiply = CTkButton(
    nums, text="*", width=85, height=85, font=sf, fg_color=green, hover_color=hover, text_color=text_color
)
b_multiply.grid(
    row=2, column=3, padx=5, pady=5
)
b_multiply.bind("<Button-1>", click)

b_divide = CTkButton(
    nums, text="/", width=85, height=85, font=sf, fg_color=green, hover_color=hover, text_color=text_color
)
b_divide.grid(
    row=3, column=3, padx=5, pady=5
)
b_divide.bind("<Button-1>", click)

b_eq = CTkButton(
    nums, text="=", width=85, height=85, font=sf, fg_color=green, hover_color=hover, text_color=text_color
)
b_eq.grid(
    row=3, column=2, padx=5, pady=5
)
b_eq.bind("<Button-1>", calculate)

# * Function Buttons
b_clear = CTkButton(
    nums, text="C", width=180, height=85, font=sf, fg_color=red, hover_color=hover, text_color=text_color
)
b_clear.grid(
    row=4, column=0, padx=5, pady=5, columnspan=2
)
b_clear.bind("<Button-1>", clear)

b_back = CTkButton(
    nums, text="X", width=180, height=85, font=sf, fg_color=red, hover_color=hover, text_color=text_color
)
b_back.grid(
    row=4, column=2, padx=5, pady=5, columnspan=2
)
b_back.bind("<Button-1>", backspace)

# ! Run the UI
root.mainloop()