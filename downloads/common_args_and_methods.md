
# 📦 PyCTK Common Widget Arguments & Methods

This sheet contains the **universal arguments and methods** shared by most widgets in the `CustomTkinter` (PyCTK) library.

Use this as a **base reference** to speed up development, documentation, and UI kit creation.

---

## 🧩 Common Initialization Arguments

These can be passed during widget creation (e.g., `CTkButton(...)`, `CTkLabel(...)`).

| Argument         | Type              | Description |
|------------------|-------------------|-------------|
| `master`         | Widget             | Parent widget or container |
| `width`          | `int`              | Widget width (in pixels) |
| `height`         | `int`              | Widget height (in pixels) |
| `corner_radius`  | `int`              | Radius for rounded corners |
| `border_width`   | `int`              | Thickness of border |
| `fg_color`       | `str/tuple`        | Background color |
| `bg_color`       | `str/tuple`        | Parent background color (auto inherited if not given) |
| `text_color`     | `str/tuple`        | Font color for text |
| `font`           | `tuple/str`        | Font family and size e.g., `("Arial", 14)` |
| `state`          | `"normal"` / `"disabled"` | Enable/disable the widget |
| `hover_color`    | `str/tuple`        | Color on hover effect |
| `text`           | `str`              | Text displayed in the widget |
| `image`          | `CTkImage` / `PhotoImage` | Optional image |
| `compound`       | `"top"`, `"bottom"`, `"left"`, `"right"` | Position of image relative to text |
| `anchor`         | `"center"`, `"w"`, `"e"`, etc. | Text alignment inside the widget |
| `command`        | `function`         | Function to call on user interaction (button, checkbox, etc.) |

> ⚠️ Some arguments are only used in interactive or text-based widgets.

---

## 🔧 Common Methods

These methods are available to **most CTk widgets**.

| Method | Description |
|--------|-------------|
| `.configure(**kwargs)` | Update widget properties dynamically |
| `.cget("option")`      | Get the current value of a configuration option |
| `.pack(**kwargs)`      | Add widget to layout using pack manager |
| `.grid(**kwargs)`      | Add widget to layout using grid manager |
| `.place(**kwargs)`     | Add widget using absolute placement |
| `.destroy()`           | Destroys the widget |
| `.bind(event, callback)` | Bind a function to an event (e.g., `<Enter>`, `<Button-1>`) |

---

## 🧠 Value Access Methods (For Input Widgets)

Used with widgets like Entry, Textbox, ComboBox, Checkbox, etc.

| Method | Description |
|--------|-------------|
| `.get()`       | Retrieve current value from the widget |
| `.set(value)`  | Set value programmatically (if applicable) |
| `.insert(index, text)` | Insert text (Entry/Textbox) |
| `.delete(start, end)` | Delete text in a range |
| `.focus_set()` | Focus the widget (Entry/Textbox) |
| `.select()` / `.deselect()` | Toggle widget selection (Checkbox/Radio) |
| `.toggle()`     | Flip current value (Switch/Checkbox) |

---

## 💡 Recommended Usage Pattern

```python
from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()

        base_style = {
            "fg_color": "#1a1a1a",
            "text_color": "#ffffff",
            "corner_radius": 8,
            "font": ("Poppins", 14)
        }

        self.button = CTkButton(self, text="Click Me", command=self.on_click, **base_style)
        self.button.pack(pady=20)

    def on_click(self):
        print("Button clicked!")

app = App()
app.mainloop()
```

---

## 🔗 Pro Tip

Use this sheet as a reference when:
- Documenting each widget
- Creating reusable components
- Teaching widget behavior in your UI series
- Building your PyCTK UI Kit or widget builder tools

---

PyCODE | 2025 | PyCTK