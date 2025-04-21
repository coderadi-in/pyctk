# CTkLabel Documentation

## Overview
`CTkLabel` is a widget of `customtkinter` that is used to diplay text or image is `CTk` window.

This documentation provides an in-depth explanation of all constructor arguments, attributes, and methods associated with `customtkinter.CTkLabel`.

- [CTkLabel Arguments](#ctklabel-arguments)
- [CTkLabel Methods](#ctklabel-methods)
- [Additional Details](#additional-details)

## Creating CTkLabel

```python
label = CTkLabel(root, text="Hello World")
```

## CTkLabel Arguments

Argument | Description | Type
-|-|-
master | The container where the widget will be displayed. e.g: `CTk`, `CTkFrame`, `CTkTopLevel`. | `Widget`
text | The text of Label. | `str`
width | Width of the Widget in px. | `int`
height | Height of the Widget in px. | `int`
corner_radius | Curves of the Corners in px. | `int`
fg_color | Background color of `CTkLabel` widget.| `str`/`tuple`
text_color | Color of Text. | `str`/`tuple`
text_color_disabled | Color of Disabled Text. | `str`/`tuple`
font | Font of Text | `tuple`/`CTkFont`
anchor | Postition of Text. e.g `n`, `center` | `str`
image | Image to display before or without text. | `CTkImage`
padx | Padding in x (horizontal) direction. | `int`
pady | Padding in y (vertical) direction. | `int`

## CTkLabel Methods

The `CTkLabel` widget don't have any specific method for itself. It only have the common arguments and methods. 

The documentation of common arguments and methods will be provided soon.

## Additional Details
- [Custom TKinter Official Documentation](https://customtkinter.tomschimansky.com/documentation/widgets/label)
- [Git Repo](https://github.com/py-developer-adi/pyctk)

---
PyCODE | 2025 | PyCTK