# Python Flet Application – Beginner Setup & Usage Guide

This guide is written for beginner students who want to **install Flet correctly**, **set up a virtual environment**, **run apps with hot reload**, and **build apps for desktop, web, and mobile**.

---

## 1. Prerequisites

Before starting, make sure you have:

* **Python 3.9 or later** installed
* Python added to **PATH**
* Internet connection

Verify Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

## 2. Create a Project Folder

Create a new folder for your Flet app:

```bash
mkdir my_flet_app
cd my_flet_app
```

---

## 3. Create a Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated and avoids conflicts.

### Create venv

**Windows**:

```bash
python -m venv venv
```

**Linux / macOS**:

```bash
python3 -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

If activation is blocked:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Windows (CMD)

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

After activation, you should see `(venv)` in your terminal.

---

## 5. Select Virtual Environment Interpreter (VS Code)

If you are using **VS Code**:

1. Press `Ctrl + Shift + P`
2. Select **Python: Select Interpreter**
3. Choose:

   * `venv\\Scripts\\python.exe` (Windows)
   * `venv/bin/python` (Linux/macOS)

This ensures VS Code runs code using the virtual environment.

---

## 6. Install Flet (Latest Version)

### Recommended (All features)

```bash
pip install flet[all] --upgrade
```

This installs:

* Core Flet
* Web support
* Desktop packaging
* Mobile build dependencies (where applicable)

### Check Installed Version

```bash
flet --version
```

### View Version History

You can track versions and changes here:

* [https://pypi.org/project/flet/#history](https://pypi.org/project/flet/#history)

---

## 7. Create a Flet App Structure

Recommended project structure:

```text
my_flet_app/
│
├── src/
|   └── assets
|   └── pages
|   └── shortcuts
│   └── main.py
│
├── venv/
└── pyproject.toml
```

### Example `main.py`

```python
import flet as ft

def main(page: ft.Page):
    page.title = "My First Flet App"
    page.add(ft.Text("Hello, Flet!"))

ft.run(main)
```

---

## 8. Run the Flet App

### Run as Desktop App

```bash
flet run src/main.py
```

or (default file):

```bash
flet run
```

---

## 9. Hot Reload & Debug Options (Very Important)

### Enable Hot Reload

Automatically reloads app on file changes:

```bash
flet run src/main.py -r
```

### Run in Debug Mode

```bash
flet run src/main.py -d
```

### Debug + Hot Reload (Recommended for Development)

```bash
flet run src/main.py -d -r
```

---

## 10. Run as Web Application

```bash
flet run src/main.py --web
```

With hot reload:

```bash
flet run src/main.py --web -r
```

---

## 11. Using `uv` (Optional Advanced Runner)

If you are using **uv**:

### Desktop

```bash
uv run flet run
```

### Web

```bash
uv run flet run --web
```

---

## 12. Build the Application (Production)

### Android (APK)

```bash
flet build apk -v
```

### iOS (IPA – macOS required)

```bash
flet build ipa -v
```

### Windows

```bash
flet build windows -v
```

### macOS

```bash
flet build macos -v
```

### Linux

```bash
flet build linux -v
```

> Note: Mobile and desktop builds may require additional SDKs (Android Studio, Xcode, etc.)

---

## 13. Common Beginner Tips

* Always activate `venv` before running the app
* Use `-r` during development for fast feedback
* Use `-d` to debug errors
* Keep `main.py` clean and modular
* Prefer SQLite for local apps

---

## 14. Helpful Resources

* Flet Documentation: [https://docs.flet.dev/](https://docs.flet.dev/)
* Getting Started: [https://docs.flet.dev/docs/](https://docs.flet.dev/docs/)
* Android Packaging: [https://docs.flet.dev/publish/android/](https://docs.flet.dev/publish/android/)
* iOS Packaging: [https://docs.flet.dev/publish/ios/](https://docs.flet.dev/publish/ios/)

---

**This guide covers everything a beginner needs to install, run, debug, and build a Flet application.**
