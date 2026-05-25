# Helpful CLI Assistant 🤖

A smart, interactive, and colorful Command-Line Interface (CLI) assistant designed to help users efficiently manage their contacts, notes, and daily schedules. Built entirely in Python using Object-Oriented Programming (OOP) principles, this application ensures data persistence and provides an intuitive user experience directly from the terminal.

---

## 🚀 Key Features

- **Advanced Contact Management**: Create, edit, and delete contact cards with structured fields, including:
  - Full Name
  - Multiple Phone Numbers (with validation)
  - Email Addresses
  - Birthdays (with upcoming anniversary tracking)
- **Built-in Notes System**: Add, organize, and quickly retrieve notes tied to specific entries or tasks.
- **Robust Data Persistence**: All information is automatically saved and loaded using a local JSON database (`messages.json`), preventing any data loss between sessions.
- **Unique ID Generation**: Utilizes a dedicated ID utility (`id_generator.py`) to guarantee conflict-free, secure indexing for every record.
- **Vibrant Terminal UX**: Powered by `Colorama` to provide a visually clean, color-coded, and highly readable terminal interface.

---

## 📂 Project Structure

The project follows clean code practices and separation of concerns:

- `main.py` — The main entry point of the application. It handles the primary user execution loop, command parsing, and orchestrates actions.
- `classes.py` — The structural core. Contains OOP models such as `AddressBook`, `Record`, and specific data validation fields.
- `id_generator.py` — A utility script dedicated to generating secure, unique identifiers for records.
- `printer_functions.py` — The presentation layer. Manages all styled, colored terminal outputs using `Colorama`.
- `messages.json` — The lightweight file-based database where application state and user records are stored.

---

## 🛠️ Installation, Setup & Usage

```bash
# ==========================================
# 1. CLONE THE REPOSITORY
# ==========================================
git clone [https://github.com/ete9nal/helpful_bot.git](https://github.com/ete9nal/helpful_bot.git)
cd helpful_bot

# ==========================================
# 2. SET UP A VIRTUAL ENVIRONMENT
# ==========================================
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# ==========================================
# 3. INSTALL DEPENDENCIES
# ==========================================
pip install -r requirements.txt

# ==========================================
# 4. RUN THE APPLICATION
# ==========================================
python main.py
