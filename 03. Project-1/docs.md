
# Language Translator App

A minimal and elegant GUI-based translator app using CustomTkinter and Google Translate. This tool takes user input, translates it from English to Hindi, and displays both the translated text and its pronunciation.

---

## 1. Overview

This is a simple **Language Translator** built using:
- `CustomTkinter` for the modern UI
- `googletrans` for real-time language translation
- `asyncio` and `threading` to handle non-blocking translations

Developed by **@_py.code (PyCODE)** as a part of a Python UI learning journey and showcased on Instagram.

---

## 2. Installation

Make sure you have Python installed. Then, install the required packages:

```bash
pip install customtkinter
pip install googletrans==4.0.0-rc1
```

> Note: `requirements.txt` is not included. Install packages manually. I'll be good for your learning.

---

## 3. The Frontend (UI)

The frontend is built using **CustomTkinter** and consists of:
- An entry box for input text (`inp`)
- A "Translate" button (`btn`)
- An output box to show translated text (`out_text`)
- A pronunciation box to show pronunciation (`pro_text`)

All elements are stacked vertically using `.pack()` and styled with modern colors and fonts.

---

## 4. The Backend (Translation Logic)

The backend logic is inside `tool.py`, using:
- `googletrans.Translator` to translate text
- A custom class `TranslationResult` to return output and pronunciation
- Thread-local event loop management for handling async calls in GUI

The `translate()` function takes `text`, translates it from **English to Hindi**, and returns both the translated output and pronunciation.

---

## 5. Functions

### `ui_translate()`
- Gets input from the entry field
- Calls `tool.translate()`
- Clears the output boxes
- Displays the result and pronunciation

### `translate()`
- Uses Google Translate under the hood
- Handles async operations within a GUI using `threading.local()` and `asyncio`

---

## 6. Architecture

```
main.py
 └── GUI Components
 └── ui_translate() –> Calls tool.translate()

tool.py
 └── translate() –> Uses Google Translate API
     └── Returns output + pronunciation
```

---

## 7. Usage

1. Run `main.py`
2. Enter text in English
3. Click "Translate"
4. See the result in Hindi and pronunciation below

---

## 8. Showcase

This app was featured on **@_py.code** Instagram to demonstrate:
- Python GUI building
- Asynchronous functions in Tkinter
- Mini-project deployment strategy

---

## 9. Future Enhancements

- Add language dropdowns for more flexibility
- Copy-to-clipboard buttons
- Save translation history
- Add support for voice input/output

---

## 10. Credits

**Developed by:** PyCODE  
**Instagram:** [@_py.code](https://www.instagram.com/_py.code)

---

PyCODE | 2025 | PyCTK
