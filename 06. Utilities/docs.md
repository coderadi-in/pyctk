# CustomTkinter Utility Classes Documentation

## 1. CTkImage

### 1.1 Overview

`CTkImage` is a utility class provided by the CustomTkinter library for handling images with built-in support for light and dark themes. Unlike the standard `PhotoImage` in Tkinter, `CTkImage` allows you to define separate image assets for both themes, providing a more cohesive and visually adaptable UI.

### 1.2 Use-Case

Here's the basic syntax for using `CTkImage`:

```python
from customtkinter import CTkImage
from PIL import Image

image = CTkImage(light_image=Image.open("light.png"),
                 dark_image=Image.open("dark.png"),
                 size=(30, 30))
```

You can then assign this image to CTk widgets such as buttons or labels:

```python
CTkButton(master=root, image=image, text="Button with Icon").pack()
```

### 1.3 Arguments and Methods

**Constructor Arguments:**

* `light_image` (PIL.Image): Image used in light mode.
* `dark_image` (PIL.Image): Image used in dark mode.
* `size` (tuple): Desired size of the image in (width, height).
* `scale` (float): Optional. If specified, scales the image by a factor.

**Methods:**

* `.configure()`: Reconfigure image attributes.
* `.image`: Access current image depending on theme.

### 1.4 Example Codes

**Example 1: Simple icon on a button**

```python
from customtkinter import CTk, CTkButton, CTkImage
from PIL import Image

app = CTk()
icon = CTkImage(light_image=Image.open("light_icon.png"),
                dark_image=Image.open("dark_icon.png"),
                size=(20, 20))
CTkButton(app, image=icon, text="Click Me").pack(pady=10)
app.mainloop()
```

**Example 2: Image scaling**

```python
image = CTkImage(light_image=Image.open("icon.png"),
                 dark_image=Image.open("icon.png"),
                 scale=0.5)
```

**Example 3: Applying on CTkLabel**

```python
from customtkinter import CTkLabel
label = CTkLabel(app, image=icon, text="")
label.pack()
```

---

## 2. CTkFont

### 2.1 Overview

`CTkFont` is CustomTkinter's dedicated utility class for managing and customizing fonts. It wraps around Tkinter's native font system but provides a cleaner and more scalable way to define font styles consistently across your CTk UI.

### 2.2 Use-Case

Basic syntax:

```python
from customtkinter import CTkFont

font = CTkFont(family="Arial", size=14, weight="bold")
CTkLabel(master=root, text="Custom Font", font=font).pack()
```

### 2.3 Arguments and Methods

**Constructor Arguments:**

* `family` (str): Font family (e.g., "Arial", "Helvetica").
* `size` (int): Font size in points.
* `weight` (str): "normal" or "bold".
* `slant` (str): "roman" or "italic".
* `underline` (bool): Underline the text.
* `overstrike` (bool): Strikethrough the text.

**Methods:**

* `.configure()`: Modify font configuration.
* `.actual()`: Returns current font attributes.
* `.cget()`: Returns the value of a specific font option.

### 2.4 Example Codes

**Example 1: Basic custom font on label**

```python
from customtkinter import CTk, CTkLabel, CTkFont

app = CTk()
font = CTkFont(family="Arial", size=16, weight="bold")
CTkLabel(app, text="Bold Arial Text", font=font).pack(pady=10)
app.mainloop()
```

**Example 2: Italic and underlined text**

```python
font = CTkFont(family="Helvetica", size=14, slant="italic", underline=True)
CTkLabel(master=root, text="Italic Underlined Text", font=font).pack()
```

**Example 3: Overstruck text**

```python
font = CTkFont(family="Times New Roman", size=12, overstrike=True)
CTkLabel(master=root, text="Strikethrough Text", font=font).pack()
```

---

This documentation gives you a concise reference for working with `CTkImage` and `CTkFont` to build a dynamic and visually adaptive UI using CustomTkinter.

---

PyCODE | 2025 | PyCTK