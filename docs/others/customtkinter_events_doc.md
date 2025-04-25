# CustomTkinter Event Binding Documentation

## 1. Overview

In `CustomTkinter`, **events** are user interactions with the GUI, such as mouse clicks, key presses, or window actions. Event binding allows developers to attach **functions (callbacks)** that respond when these events occur.

Events are essential for creating interactive applications. Whether it's validating a form on a button click, opening a menu on right-click, or responding to keyboard shortcuts, events provide the flexibility and power needed in GUI development.

## 2. Event Binding

To bind an event in CustomTkinter (inherits from tkinter), you use the `widget.bind()` method:

```python
import customtkinter as ctk

def on_click(event):
    print("Widget clicked!")

root = ctk.CTk()
button = ctk.CTkButton(root, text="Click Me")
button.bind("<Button-1>", on_click)
button.pack()
root.mainloop()
```

## 3. Events

| Event            | Description                           | Common Use Case                         |
|------------------|---------------------------------------|------------------------------------------|
| `<Button-1>`     | Left mouse button click               | Trigger button actions                   |
| `<Button-2>`     | Middle mouse button click             | Custom gestures or advanced controls     |
| `<Button-3>`     | Right mouse button click              | Open context menu                        |
| `<Double-Button-1>` | Double left-click                  | Open file, zoom in, etc.                 |
| `<Enter>`        | Cursor enters widget                  | Highlight widget                         |
| `<Leave>`        | Cursor leaves widget                  | Revert highlight                         |
| `<Motion>`       | Mouse movement over widget            | Track cursor, draw apps                  |
| `<Key>`          | Any key is pressed                    | Input handling, shortcuts                |
| `<KeyPress-A>`   | Specific key press (e.g. "A")         | Game controls, text shortcuts            |
| `<FocusIn>`      | Widget gets focus                     | Highlight or validate input              |
| `<FocusOut>`     | Widget loses focus                    | Save or reset input                      |
| `<Configure>`    | Widget is resized or moved            | Responsive design adjustments            |
| `<MouseWheel>`   | Mouse scroll                          | Zoom or scroll views                     |

## 4. Binding Examples

### Example 1: Binding a Button Click
```python
def on_click(event):
    print("Button clicked")

button.bind("<Button-1>", on_click)
```

### Example 2: Binding a Keyboard Shortcut
```python
def on_key(event):
    print(f"Key pressed: {event.char}")

entry.bind("<Key>", on_key)
```

### Example 3: Mouse Hover Effect
```python
def on_hover(event):
    button.configure(fg_color="lightblue")

def on_leave(event):
    button.configure(fg_color="white")

button.bind("<Enter>", on_hover)
button.bind("<Leave>", on_leave)
```

## 5. Event Object

Every bound function receives an `event` object that contains useful information:

- `event.x`, `event.y`: Mouse coordinates
- `event.char`: Character of key pressed
- `event.keysym`: Symbolic name of key (e.g. "Return")
- `event.widget`: The widget that triggered the event

Example:
```python
def show_info(event):
    print(f"Clicked at: ({event.x}, {event.y}) on {event.widget}")
```

## 6. Tips for Event Handling

- **Use `lambda`** for passing arguments: `button.bind("<Button-1>", lambda e: handler(arg))`
- **Unbind an event**: `widget.unbind("<EventName>")`
- **Bind to all widgets**: Use `root.bind_all("<Key>", callback)`

---

This concise reference will help you confidently implement event-driven logic in your `CustomTkinter` apps.

PyCODE | 2025 | PyCTK