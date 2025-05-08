## CTkRadioButton

### 1.1 Overview

`CTkRadioButton` is a customizable radio button widget in CustomTkinter that allows users to select a single option from a set. It supports CustomTkinter’s theming system and is ideal for building consistent UIs that need exclusive selections.

### 1.2 Use-Case

Basic syntax:

```python
from customtkinter import CTkRadioButton

radio_button = CTkRadioButton(master=root, text="Option A", variable=var, value="A")
radio_button.pack()
```

### 1.3 Arguments and Methods

**Constructor Arguments:**

* `master`: Parent widget.
* `text` (str): Label displayed next to the radio button.
* `variable` (tk.Variable): Shared variable among radio buttons in the group.
* `value` (any): The value that this button sets when selected.
* `command` (function): Function called when the button is selected.
* `hover` (bool): Enables hover effects.

**Methods:**

* `.select()`: Programmatically select the radio button.
* `.deselect()`: Programmatically deselect the radio button.
* `.toggle()`: Toggle the selection state.
* `.get()`: Get the current value of the radio button.
* `.configure()`: Modify widget options.

### 1.4 Example Codes

**Example 1: Basic radio button group**

```python
import tkinter as tk
from customtkinter import CTk, CTkRadioButton

app = CTk()
var = tk.StringVar(value="A")

CTkRadioButton(app, text="Option A", variable=var, value="A").pack()
CTkRadioButton(app, text="Option B", variable=var, value="B").pack()
app.mainloop()
```

**Example 2: Command callback on selection**

```python
import tkinter as tk
from customtkinter import CTk, CTkRadioButton

def on_select():
    print("Selection changed")

app = CTk()
var = tk.StringVar()
CTkRadioButton(app, text="Select Me", variable=var, value="Yes", command=on_select).pack()
app.mainloop()
```

**Example 3: Default selected option**

```python
import tkinter as tk
from customtkinter import CTk, CTkRadioButton

app = CTk()
var = tk.StringVar(value="B")

CTkRadioButton(app, text="Option A", variable=var, value="A").pack()
CTkRadioButton(app, text="Option B", variable=var, value="B").pack()
app.mainloop()
```
---

PyCODE | 2025 | PyCTK