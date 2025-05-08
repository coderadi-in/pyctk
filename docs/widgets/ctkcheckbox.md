## CTkCheckBox

### 1.1 Overview

`CTkCheckBox` is a customizable checkbox widget provided by CustomTkinter. It allows you to create interactive checkbox elements with support for theme adaptation, state handling, and consistent UI styling.

### 1.2 Use-Case

Basic syntax:

```python
from customtkinter import CTkCheckBox

checkbox = CTkCheckBox(master=root, text="Accept Terms")
checkbox.pack()
```

### 1.3 Arguments and Methods

**Constructor Arguments:**

* `master`: Parent widget.
* `text` (str): Text displayed beside the checkbox.
* `command` (function): Function to execute when checkbox is toggled.
* `variable` (tk.IntVar): Variable linked to checkbox state.
* `onvalue` (int): Value when checkbox is selected (default is 1).
* `offvalue` (int): Value when checkbox is deselected (default is 0).
* `hover` (bool): Enables hover effects.

**Methods:**

* `.select()`: Programmatically check the box.
* `.deselect()`: Programmatically uncheck the box.
* `.toggle()`: Toggle the state of the checkbox.
* `.get()`: Return current state value.
* `.configure()`: Modify widget configuration.

### 1.4 Example Codes

**Example 1: Basic checkbox with command**

```python
from customtkinter import CTk, CTkCheckBox

def on_toggle():
    print("Checkbox toggled")

app = CTk()
cb = CTkCheckBox(app, text="I agree", command=on_toggle)
cb.pack(pady=10)
app.mainloop()
```

**Example 2: Checkbox with IntVar**

```python
import tkinter as tk
from customtkinter import CTk, CTkCheckBox

app = CTk()
var = tk.IntVar()
CTkCheckBox(app, text="Enable feature", variable=var).pack()
app.mainloop()
```

**Example 3: Toggle programmatically**

```python
from customtkinter import CTk, CTkCheckBox

app = CTk()
cb = CTkCheckBox(app, text="Auto-toggle")
cb.pack()
cb.select()  # Set as selected on load
app.mainloop()
```
---

PyCODE | 2025 | PyCTK