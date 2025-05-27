# Packaging a CustomTkinter App into an Executable &bull; PyCODE

This guide explains how to convert a Python script (.py) using CustomTkinter into a standalone Windows executable (.exe) with PyInstaller, including icons and additional data files.

## Prerequisites

- Python installed (≥ 3.6)
- customtkinter installed:

```bash
pip install customtkinter
```

PyInstaller installed:
```bash
pip install pyinstaller
```

## Step 1: Prepare Your Project
Assume your project structure looks like this:

```
my_app/
│── main.py          # Your CustomTkinter script
└── icon.ico         # App icon (optional)
```

## Step 2: Modify Your Script for Packaging

Ensure file paths are compatible with the packaged app. Use the following approach for resource loading:

```python
import os
import sys
import customtkinter as ctk

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller temporary folder
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Example usage:
icon_path = resource_path("icon.ico")
config_path = resource_path("data/config.json")

app = ctk.CTk()
app.iconbitmap(icon_path)  # Set window icon
app.mainloop()
```

## Step 3: Create a PyInstaller Spec File (Optional)
For advanced configurations, generate a spec file:

```bash
pyinstaller --name MyApp --onefile --windowed main.py
```

This creates main.spec. Edit it to include data files:

```python
# main.spec
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.ico', '.'), ('data/config.json', 'data')],  # Add files here
    hiddenimports=[],
    hookspath=[],
    ...
)
```

## Step 4: Run PyInstaller

### Basic Command (One-File Executable):

```bash
pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --add-data "data/config.json;data" main.py
```

- --onefile: Bundles everything into a single .exe.
- --windowed: Prevents a console window from appearing.
- --icon: Sets the .exe icon.
- --add-data: Includes additional files (format: "source;destination").

### Using a Spec File:

```bash
pyinstaller main.spec
```

## Step 5: Locate the Executable

After running PyInstaller:
- One-file executable: dist/main.exe
- Folder with dependencies: dist/main/

## Troubleshooting
1. Missing Files: Ensure all paths are correct in --add-data.
2. Antivirus False Positives: Some AVs flag PyInstaller executables. Whitelist if needed.
3. Console Window: Use --windowed to hide it.

### Conclusion
You now have a standalone .exe for your CustomTkinter app! Test it on a machine without Python to verify dependencies. For further optimizations, refer to the [PyInstaller Documentation](https://pyinstaller.org/en/stable/).

---

PyCODE &bull; 2025 &bull; PyCTK