## CTkSegmentedButton

### 1. Overview

`CTkSegmentedButton` is a segmented control widget in CustomTkinter that allows users to switch between a small number of mutually exclusive options. It is ideal for toggling between views, filters, or modes. Unlike a dropdown or combo box, all options are visibly laid out, improving accessibility and user experience.

Use it when you want quick switching with visible states — such as in dashboards, theme selectors, or filter controls.

---

### 2. Attributes

**Constructor Attributes:**

* `master`: Parent widget.
* `values` (list\[str]): The segments shown as options.
* `command` (function): Function called with selected value when a segment is clicked.
* `variable` (tk.StringVar): Variable to bind the selection.
* `width` / `height` (int): Dimensions of the widget.
* `selected_color` (str): Background color of selected segment.
* `unselected_color` (str): Background color of unselected segments.
* `text_color` (str): Font color.
* `corner_radius` (int): For rounded edges.

---

### 3. Methods

* `.get()`: Returns the current selected value.
* `.set(value)`: Programmatically selects a segment.
* `.configure()`: Modify properties after creation.
* `.cget(option_name)`: Gets current value of an option.

---

### 4. Example Code Snippets

**Example 1: Basic usage**

```python
from customtkinter import CTk, CTkSegmentedButton

app = CTk()
seg = CTkSegmentedButton(app, values=["Light", "Dark", "System"])
seg.pack(pady=10)
app.mainloop()
```

**Example 2: Using command**

```python
def theme_selected(choice):
    print(f"Selected theme: {choice}")

seg = CTkSegmentedButton(app, values=["A", "B"], command=theme_selected)
seg.pack()
```

**Example 3: Using with StringVar**

```python
import tkinter as tk
var = tk.StringVar(value="Light")
seg = CTkSegmentedButton(app, values=["Light", "Dark"], variable=var)
seg.pack()
```

---

### 5. Best Practices

* Use when options are limited and switching needs to be fast.
* Always provide visual feedback with selection colors.
* Pair with `StringVar` to track state and bind logic.
* Avoid clutter: keep option text concise.

---

### 6. When Not to Use

* When options exceed 4–5 items — consider `CTkComboBox`.
* When space is tight and minimal UI is a priority.

---

### 7. Summary

`CTkSegmentedButton` is a stylish, functional alternative to dropdowns and radio buttons. It encourages fast selection, clear UI design, and better interaction on desktop apps. Ideal for modern UIs built with CustomTkinter.

---

PyCODE | 2025 | PyCTK