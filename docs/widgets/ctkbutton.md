# CTkButton

## Overview
`CTkButton` is a modern, customizable button widget in the `customtkinter` library. It supports themes, hover effects, customizable colors, and integrates seamlessly with standard Tkinter. Ideal for creating visually appealing GUI applications.

## Creating CTkButton

```python
button = CTkButton(master=root, text="Click Me", command=callback)
```

## Arguments

Widget | Description
-|-
master `Widget` | Parent widget (e.g., `CTk()` window or a frame).
text `str` | Text displayed on the button (default: `""`).
command `function` | Function/method called when the button is clicked.
width `int` | Button width in pixels (default: `140`).
height `int` | Button height in pixels (default: `28`).
fg_color `str`/`tuple` | Button color (e.g., `"green"`, `("#FF0000", "#00FF00")` for light/dark mode).
hover_color `str`/`tuple` | Color on hover (default: darkens `fg_color`).
border_color `str`/`tuple` | Border color (default: `fg_color`).
border_width `int` | Border thickness (default: `0`).
corner_radius `int` | Rounded corners radius (default: `None`).
text_color `str`/`tuple` | Text color (default: `"white"`).
font `tuple`/`CTkFont` | Font style (e.g., `("Arial", 12, "bold")`).
state `str` | `"normal"` (clickable) or `"disabled"` (grayed out).
anchor `str` | Text position (e.g., `"w"` for left-aligned).

## Methods

- `.configure(**kwargs)`: Update button properties (e.g., `button.configure(text="New Text", fg_color="blue")`).
- `.cget(parameter)`: Get the current value of a parameter (e.g., `button.cget("fg_color")`).
- `.invoke()`: Trigger the button’s command programmatically.
- `.bind(event, handler)`: Bind events (e.g., `<Enter>` for mouse hover).
- `.pack()`, `.place()`, `.grid()`: Standard geometry management methods.
- `.destroy()`: Remove the button from the UI.

## Configuration Examples

```python
# Disable the button and change color  
button.configure(state="disabled", fg_color="gray")

# Add a border and rounded corners  
button.configure(border_width=2, border_color="black", corner_radius=10)
```

## Events and Bindings

```python
def hover(event):
    print("Mouse over button!")

button.bind("<Enter>", hover)  # Bind hover event
```

## TroubleShooting

- Command not working? Ensure command is a `function` (not a function call).
- Button not visible? Check geometry management (`pack()`, `grid()`, etc.).
- Colors not updating? Use valid color codes (hex or named colors).

## Additional Details
- [CTkButton Widget Docs](https://customtkinter.tomschimansky.com/documentation/widgets/button)
- [Git Repo](https://github.com/py-developer-adi/pyctk)

---
PyCODE | 2025 | PyCTK