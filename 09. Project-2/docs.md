# A Calculator App &bull; PyCODE

This is a basic app that performs arithmetical calculations, It also serves as a learning tool for UI development with Python. We've also packaged this app to make it distributable, allowing it to run as a native desktop application without requiring a Python interpreter or code editors like Visual Studio. Let's go through all the code blocks of this app.

## Table of Contents
- [UI Widgets](#ui-widgets)
  - [The Display](#the-display)
  - [The Keypad](#the-keypad)
  - [Buttons](#buttons)
- [The Backend](#the-backend)
- [Packaging](#packaging)

# Developer's Documentation

## UI Widgets

The UI of this app is divided into two main sections: One for the display, where the output will be shown, and the keypad where all the buttons are placed.

### The Display

```python
# | Display
display = CTkEntry(root, width=380, height=70, font=lf)
display.grid(row=0, column=0, padx=10, pady=10)
```

**Purpose:** The display shows the buttons pressed by the user and the results of arithmetical calculations.

### The Keypad

```python
# | Keypad
nums = CTkFrame(root, width=380, height=490)
nums.grid(row=1, column=0, padx=10, pady=10)
```

**Purpose:** The keypad frame holds all the buttons inside it, While it's not strictly necessary to place buttons inside a frame, doing so improves code organization and maintainability.

### Buttons

```python
b1 = CTkButton(
    nums, text="1", width=85, height=85, font=sf, fg_color=blue, hover_color=hover, text_color=text_color
)
b1.grid(row=0, column=0, padx=5, pady=5)
b1.bind("<Button-1>", click)
```

## The Backend

Here's the main logic of how and why our app is working and doing arithmetical calculations.

### The `click()` Function

```python
def click(event):
    widget = event.widget
    button = widget.master
    text = button.cget("text")
    display.insert(END, text)
```

This function is triggered when the user clicks any numerical button or operation button. This function shows the clicked button on the display. Let's break down each line of the function.

**`widget = event.widget`**: This line gets the current widget which was clicked.

**`button widget.master`**: The `widget` variable holds a canvas, and the button lies behind it. We use the `.master` attribute to access the button.

**`text = button.cget("text")`**: This line gets us the text of the button, as we know that `.cget()` is used to get the value of any attribute of any widget.

**`display.insert(END, text)`**: This line inserts the text that we got from the button to the display.

### The `clear()` Function

```python
def clear(event):
    display.delete(0, END)
```

This function is triggered when the user clicks the clear button and in some other functions to clear the display. As the name suggest, it's work is to clear the display, means remove all text. Let's break it down.

**`display.delete(0, END)`**: This line deletes the text of display from `0` (start) to `END`.

### The `calculate()` Function

```python
def calculate(event):
    query = display.get()
    try:
        res = eval(query)
    except Exception as e:
        res = "Error"
        print(e)

    clear(None)
    display.insert(0, res)
```

This is the main function of our UI, it calculates the problem of display and it shows `Error` text if there's an issue in the text. Let's break it down.

**`query = display.get()`**: This line gets the text of display.

**`res = eval(query)`** This line tries to evaluate the text as an arithmetical problem as `res`.

**`res = "Error"`**: This line sets the `res` (result) as `"Error"`. Because this line is in `except` block, so it'll be executed only if there's an error.

**`print(e)`**: This line is not recommended for an .exe app, but for development, we can use it. It prints the error on console.

**`clear(None)`**: This line executes the `clear()` function with `None` as event, because there's no event here.

**`display.insert(0, res)`**: This line adds the result on the display.

### The `backspace()` Function

```python
def backspace(event):
    text = display.get()
    if len(text) > 0:
        newtext = text[:-1]
        clear(None)
        display.insert(0, newtext)
```

This function is for the X button, it deletes the last character of the display, working just like the backspace button. Here's the breakdown of each line.

**`text = display.get()`**: Gets the text of display.

**`if len(text) > 0:`**: Checks if text isn't an empty string. You can also use `if text != ''` as alternative.

**`newtext = text[:-1]`**: Creates `newtext` with all characters of text expect the last one.

**`clear(None)`** Clears the display.

**`display.insert(0, newtext)`**: Inserts the new text in the display.

## Packaging

Here's the most interesting part, because in this part, we'll pack this project to an **Application** that runs on desktop.

Run these commands in the terminal to convert your `.py` file to `.exe` app.

### Install PyInstaller Library

```shell
pip install pyinstaller
```

This library will help us to convert our `.py` file to `.exe` app.

### Convert .py to .exe

```shell
pyinstaller --onefile --windowed main.py
```

Options | Desciption
-|-
--onefile | Bind all files and build logs to one file.
--windowed | Makes the app open without console or terminal.

## Conclusion
This calculator app demonstrates the basics of UI development with `customtkinter` and packaging Python apps for distribution. Future enhancements could include adding more advanced operations or improving error handling.

---

PyCODE &bull; 2025 &bull; PyCTK