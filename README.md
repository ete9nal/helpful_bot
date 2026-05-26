# Nexus: Contacts & Notes CLI Manager

Nexus is a lightweight, high-performance Command Line Interface (CLI) CRM system built with Python. Designed with a modular, object-oriented architecture, it provides an efficient environment for managing multi-field contact directories and structured text notes with built-in data persistence and input validation.

## 🛠️ Key Features

- **Robust Contact Management:** Store and manage extensive contact profiles, including full names, validated phone numbers, emails, and birthdays.
- **Advanced Notes System:** Create, edit, and organize text notes using customizable tags for rapid searching and categorization.
- **Data Persistence:** Automatic serialization and deserialization using Python's built-in `pickle` module, ensuring your data is safely stored and restored between sessions.
- **Strict Input Validation:** Built-in validation rules for phone formats, email addresses, and date formats to prevent data corruption and ensure integrity.
- **Smart Search & Upcoming Birthdays:** Quick full-text search across all contacts and an automated utility to check for upcoming birthdays within a specific range.

## 🏗️ Architecture & Design Principles

The project strictly follows core Object-Oriented Programming (OOP) concepts:
- **Separation of Concerns:** The data layer (models like `Record`, `AddressBook`, and `Note`) is completely separated from the user interface and command-parsing logic.
- **Encapsulation:** Critical attributes (such as phones, emails, and dates) use private structures and strict validation before assignment.

## 🚀 Tech Stack

- **Core:** Python 3.10+
- **Dependency Management:** Poetry / Pip
- **Data Handling:** Native Python Serialization (`pickle`, `re`)

## 💻 Installation & Usage

1. Clone the repository:
   ```bash
      git clone [https://github.com/ete9nal/Nexus-Contacts-Notes-Manager.git](https://github.com/ete9nal/Nexus-Contacts-Notes-Manager.git)

2. Navigate to the project folder and run:
  ```bash
     python main.py
