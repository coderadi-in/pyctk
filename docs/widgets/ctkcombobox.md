## CTkComboBox

### 1.1 Overview

`CTkComboBox` is a themed drop-down menu widget provided by CustomTkinter that allows users to choose one option from a list. It combines the functionality of an entry widget and a drop-down, styled according to CustomTkinter’s appearance modes.

### 1.2 Use-Case

Basic syntax:

```python
from customtkinter import CTkComboBox

combo = CTkComboBox(master=root, values=["Option 1", "Option 2", "Option 3"])
combo.pack()
```

### 1.3 Arguments and Methods

**Constructor Arguments:**

* `master`: Parent widget.
* `values` (list): List of selectable values.
* `command` (function): Function called when selection changes.
* `variable` (tk.StringVar): Variable linked to the selected value.
* `width`, `height` (int): Dimensions of the combo box.
* `state` (str): "normal" or "readonly".

**Methods:**

* `.get()`: Returns the currently selected value.
* `.set(value)`: Sets the selected value programmatically.
* `.configure()`: Modify widget properties.
* `.focus()`: Sets focus to the widget.

### 1.4 Example Codes

**Example 1: Basic combo box**

```python
from customtkinter import CTk, CTkComboBox

app = CTk()
combo = CTkComboBox(app, values=["Python", "Java", "C++"])
combo.pack(pady=10)
app.mainloop()
```

**Example 2: Using command callback**

```python
def on_select(choice):
    print(f"Selected: {choice}")

combo = CTkComboBox(app, values=["One", "Two"], command=on_select)
combo.pack()
```

**Example 3: Linking with StringVar**

```python
import tkinter as tk

var = tk.StringVar(value="Option 1")
combo = CTkComboBox(app, values=["Option 1", "Option 2"], variable=var)
combo.pack()
```

---

PyCODE | 2025 | PyCTK