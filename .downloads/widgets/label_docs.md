# CTkLabel Documentation

## Overview

`CTkLabel` is a widget from the `customtkinter` library, which extends the standard `tkinter` module with modern styling and additional features. It is used to display static text or images within a GUI application.

This documentation provides an in-depth explanation of all constructor arguments, attributes, and methods associated with `CTkLabel`.

---

## Importing

```python
from customtkinter import CTkLabel
```

---

## Constructor

```python
CTkLabel(master=None, **kwargs)
```

### Parameters

- **master**: `Widget` (optional)
  - The parent widget in which the label will be placed.

### Keyword Arguments (kwargs)

- **text**: `str` (default="")

  - The text to be displayed in the label.

- **textvariable**: `tk.StringVar` (optional)

  - A Tkinter `StringVar` object that can be updated dynamically.

- **image**: `CTkImage` (optional)

  - A `customtkinter.CTkImage` object to display an image alongside or instead of text.

- **compound**: `str` (default="center")

  - Positioning of image relative to text. Accepts: `"top"`, `"bottom"`, `"left"`, `"right"`, `"center"`.

- **font**: `tuple | CTkFont` (optional)

  - Font style for the label text. Example: `("Arial", 14)`.

- **text\_color**: `str | tuple` (optional)

  - Color of the text. Can be a single string or a tuple for light/dark mode: `("black", "white")`.

- **anchor**: `str` (optional)

  - Text anchor alignment. Accepts `"n"`, `"ne"`, `"e"`, `"se"`, `"s"`, `"sw"`, `"w"`, `"nw"`, `"center"`.

- **width**: `int` (optional)

  - Width of the label in pixels.

- **height**: `int` (optional)

  - Height of the label in pixels.

- **corner\_radius**: `int` (default=6)

  - Corner radius for rounded rectangle label shape.

- **fg\_color**: `str | tuple | None` (optional)

  - Background color of the label. Can be string or a tuple for light/dark themes.
  - If `None`, inherits background color from parent widget.

- **bg\_color**: `str | tuple` (optional)

  - Sets the background color behind the widget, primarily for design layering.

- **state**: `str` (default="normal")

  - Label state. Accepts: `"normal"` or `"disabled"`.

- **hover\_color**: `str | tuple` (optional)

  - Background color when hovering over the label.

- **cursor**: `str` (optional)

  - Sets the cursor type when hovering over the label. Example: "hand2".

---

## Common Methods

### `.configure(**kwargs)` / `.config(**kwargs)`

Updates the label configuration after initialization.

```python
label.configure(text="Updated Text", text_color="red")
```

### `.cget("option")`

Returns the current value of the given configuration option.

```python
text = label.cget("text")
```

### `.bind(sequence, callback)`

Binds an event to the label (e.g., click, hover).

```python
label.bind("<Button-1>", lambda e: print("Clicked!"))
```

### `.destroy()`

Destroys the widget and releases its resources.

```python
label.destroy()
```

### `.pack()`, `.grid()`, `.place()`

Standard geometry managers to position the label.

```python
label.pack(padx=10, pady=10)
```

---

## Usage Example

```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x200")

label = ctk.CTkLabel(
    master=app,
    text="Hello, CustomTkinter!",
    font=("Helvetica", 16),
    text_color=("black", "white"),
    corner_radius=10,
    fg_color=("#eeeeee", "#333333"),
    width=200,
    height=50,
    anchor="center"
)
label.pack(pady=40)

app.mainloop()
```

---

## Best Practices

- Use `textvariable` when you need dynamic text updates.
- Combine `CTkImage` and `compound` to show icons with text.
- Prefer tuples for color arguments to support light/dark modes.
- Adjust `corner_radius` to match your UI style.

---

## Additional Notes

- `CTkLabel` is non-interactive by default. For clickable behavior, bind an event like `<Button-1>`.
- It inherits most `tk.Label` behaviors but supports modern theming and responsiveness.

---

## Related Widgets

- `CTkButton`
- `CTkEntry`
- `CTkTextbox`
- `CTkFrame`

For more, visit the [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/widgets/label)

---

PyCODE | 2025 | PyCTK

