# CustomTkinter Window Documentation

This document provides detailed explanations of all the arguments and methods that can be used with the `customtkinter.CTk` window.

## Table of Contents

- [CTk Window Arguments](#ctk-window-arguments)
- [CTk Window Methods](#ctk-window-methods)
- [Usage Example](#usage-example)

---

## CTk Window Arguments

The `CTk` class inherits from `tk.Tk`, but also includes additional customization provided by `customtkinter`.

```python
window = customtkinter.CTk(**kwargs)
```

### Common Arguments

| Argument             | Type      | Description |
|----------------------|-----------|-------------|
| `fg_color`           | str/tuple | Background color of the window. Accepts a single color or a tuple for light and dark modes. |
| `background_corner_colors` | tuple | Colors for the window's corner background gradient. |
| `title`              | str       | Sets the window title. |
| `iconbitmap`         | str       | Path to the icon bitmap file. |
| `geometry`           | str       | Sets the initial size of the window (e.g., `"800x600"`). |
| `resizable`          | bool/tuple| Allows window resizing in X and Y directions (e.g., `True`, or `(True, False)`). |
| `minsize`            | tuple     | Minimum size of the window `(width, height)`. |
| `maxsize`            | tuple     | Maximum size of the window `(width, height)`. |

---

## CTk Window Methods

Here are the most common methods you can use on a `CTk` window object.

### Window Control

- `title("Window Title")` – Sets the window's title.
- `geometry("widthxheight")` – Sets the size of the window.
- `resizable(width_bool, height_bool)` – Allows or disallows resizing.
- `minsize(width, height)` – Sets the minimum window size.
- `maxsize(width, height)` – Sets the maximum window size.
- `iconbitmap("icon_path.ico")` – Sets the window icon.

### Window Behavior

- `mainloop()` – Starts the Tkinter main event loop.
- `update()` – Forces a UI update.
- `destroy()` – Destroys the window.
- `deiconify()` – Restores the window from minimized state.
- `withdraw()` – Hides the window.
- `attributes("-topmost", True)` – Makes the window always on top.

### Positioning

- `winfo_screenwidth()` – Gets screen width.
- `winfo_screenheight()` – Gets screen height.
- `winfo_x()` – Gets the current x-position of the window.
- `winfo_y()` – Gets the current y-position of the window.

---

## Usage Example

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("My CustomTkinter App")
app.geometry("800x600")
app.resizable(True, False)
app.iconbitmap("icon.ico")
app.mainloop()
```

---

## Notes

- CustomTkinter follows a modern theme design for GUI elements.
- Supports dark and light modes using `ctk.set_appearance_mode("dark")`.

---

### PyCTK | PyCODE