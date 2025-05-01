# How to Build Themes for CustomTkinter

## 1. Overview: What is a Theme?

A **theme** in CustomTkinter is a customizable design configuration (usually in `.json` format) that controls the **appearance of widgets** (like labels, buttons, entries, etc.) across your entire application. Themes help you:

- Maintain **consistent styling**.
- Easily **switch between light and dark modes**.
- Share a **visual identity** across apps or projects.
- Customize UIs without hardcoding styles.

---

## 2. Theme File: Creating the JSON File

Themes in CustomTkinter are stored as JSON files. Each key in the file represents a widget class (e.g., `CTk`, `CTkLabel`), and its value is a dictionary of styling options.

Here’s an example `design.json` with minimal settings:

```json
{
    "CTk": {
        "fg_color": ["white", "black"]
    },
    "CTkLabel": {
        "corner_radius": 0,
        "text_color": ["#000000", "#FFFFFF"],
        "fg_color": "transparent"
    }
}
```

**Explanation:**
- `fg_color`: Background color for light and dark mode.
- `text_color`: Text color for widgets (light, dark).
- `"transparent"` is used when you want to inherit the background from the parent.

---

## 3. Theme Building: Defining Styles

Let’s build two example themes.

### 🎨 Example 1: Minimal Light Theme (`minimal_light.json`)
```json
{
    "CTk": {
        "fg_color": ["#f8f8f8", "#1e1e1e"]
    },
    "CTkLabel": {
        "text_color": ["#333333", "#eeeeee"],
        "fg_color": "transparent",
        "corner_radius": 0
    }
}
```

This theme applies a light background and dark text for `CTkLabel`.

### 🧛 Example 2: Dracula-Inspired Dark Theme (`dracula.json`)
```json
{
    "CTk": {
        "fg_color": ["#282a36", "#1e1f29"]
    },
    "CTkLabel": {
        "text_color": ["#f8f8f2", "#f8f8f2"],
        "fg_color": "transparent"
    }
}
```

Here we’re using Dracula theme colors. Great for dark-mode lovers!

> 💡 Pro Tip: You can keep adding more widgets like `CTkButton`, `CTkEntry`, `CTkFrame`, etc., using similar key-value pairs.

---

## 4. Importing Themes into Your App

To load and apply a custom theme, use:

```python
import customtkinter as ctk

ctk.set_default_color_theme("design.json")  # or "path/to/your/theme.json"
```

Place the `design.json` in the same directory, or provide the full path.

Then, build your UI:

```python
app = ctk.CTk()
label = ctk.CTkLabel(app, text="Hello with Theme!")
label.pack(padx=20, pady=20)
app.mainloop()
```

---

## 5. Theme Structure Best Practices

- **Always use arrays** for dual mode (`[light, dark]`) settings.
- Use `"transparent"` to inherit background where needed.
- If a color value doesn’t change across modes, duplicate it:  
  `"text_color": ["#000000", "#000000"]`

---

## 6. Widgets You Can Customize

Most commonly styled widgets:
- `CTk` (main window)
- `CTkLabel`
- `CTkButton`
- `CTkEntry`
- `CTkFrame`
- `CTkSwitch`

You can find full attribute support in the [CustomTkinter docs](https://customtkinter.tomschimansky.com/documentation/color).

---

## 7. Tips to Share with Your Audience

- Start with a **basic design** and build from there.
- Share your themes as `.json` downloads.
- Offer **light/dark toggling** for better UX.
- Keep a **theme library** for your projects.

---

PyCODE | 2025 | PyCTK