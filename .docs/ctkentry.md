# CTkEntry

## Overview
`CTkEntry` widget is used to create an input field in `customtkinter`.

This documentation provides an in-depth explanation of all constructor arguments, attributes, and methods associated with `customtkinter.CTkEntry`.

## Creating CTkEntry

```python
entry = CTkEntry(root)
```

## CTkEntry Arguments

Argument | Description | Type
-|-|-
master | The container widget where the entry should be displayed. | `Widget`
width | Used to set the width of entry. | `int`
height | Used to set the heigh of entry. | `int`
corner_radius | Used to add a curvature in the corners of entry. | `int`
fg_color | Used to set the background color of entry. | `str`/`tuple`
text_color | Used to set the color of text. | `str`/`tuple`
placeholder_text_color | Used to set the color of placeholder text. | `str`/`tuple`
placeholder_text | Used to add a placeholder. | `str`
font | It adds custom font to the entry. | `tuple`/`CTkFont`
state | Set the state to `normal` or `disabled` | `str`

## CTkEntry Methdos

### 1. **`.configure`**:
Updates the attributes of entry widget.

```python
entry.configure(fg_color="#FF00FF")
```

### 2. **`.cget`**:
Returns the current value of given attribute.

```python
print(entry.cget("state"))
```

### 3. **`.bind`**:
Used to bind an event to entry.

```python
entry.bind("<Double-1>", command)
```

### 4. **`.delete`**:
Used to delete the text in entry from index a to index (b - 1).

```python
entry.delete(3, 5)
```

### 5. **`.insert`**:
Used to insert a string at given index.

```python
entry.insert(0, "coderadi")
```

### 6. **`.get`**:
Used to get the text in entry.

```python
print(entry.get())
```

## Additional Details
- [Entry Widget Docs](https://customtkinter.tomschimansky.com/documentation/widgets/entry/)
- [Git Repo](https://github.com/py-developer-adi/pyctk)

---
PyCODE | 2025 | PyCTK