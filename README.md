# Collyers Car Park Management System

## Description

This application is a desktop utility for managing and searching records in the Collyers Car Park database. It provides a graphical user interface (GUI) to search for vehicles based on owner's name, registration number, vehicle make, and model. It also allows filtering by role (student, staff, visitor).

## Features

- Search for car park records by:
  - Owner's Name (first and/or last)
  - Vehicle Registration Number
  - Vehicle Make
  - Vehicle Model
- Filter search results by role:
  - All (default search)
  - Student
  - Staff
  - Visitor
- Display search results in a table format.
- Clear search fields.
- Case-insensitive and partial search capabilities.

## Project Structure

```
.
├── carpark.db        # SQLite database file
├── Carpark.png       # Image asset for the UI
├── carpark.ui        # Qt Designer UI file
├── main.py           # Main application logic
├── ui.py             # Python UI class generated from carpark.ui
├── .gitignore        # Git ignore file
└── __pycache__/      # Python cache directory (auto-generated)
```

## Prerequisites

- Python 3.x
- PyQt5

## Setup and Installation

1.  **Clone the repository (if applicable) or download the files.**
2.  **Ensure Python 3 is installed on your system.**
3.  **Install dependencies:**
    Open a terminal or command prompt in the project directory and run:
    ```bash
    pip install PyQt5
    ```
4.  **Database:**
    The application uses an SQLite database named `carpark.db`. This file must be present in the same directory as `main.py`. The application expects a table named `Carpark` with the following columns:
    - `registration` (TEXT)
    - `fname` (TEXT)
    - `lname` (TEXT)
    - `make` (TEXT)
    - `model` (TEXT)
    - `role` (TEXT) - e.g., 'student', 'staff', 'visitor'

## How to Run

1.  Navigate to the project directory in your terminal.
2.  Execute the main script:
    ```bash
    python main.py
    ```
    This will launch the GUI application.

## UI Overview

The user interface, defined in `carpark.ui` and utilized by `main.py`, consists of:

- Input fields for Name, Registration, Make, and Model.
- A "Search" button to perform a general search based on the input fields.
- A "Clear" button to reset the input fields.
- Buttons to filter by "Student Cars", "Staff Cars", and "Visitor Cars". _(Note: These buttons are functionally implemented in `main.py` but might need to be explicitly added to the `carpark.ui` file via Qt Designer if not already present. The `carpark.ui` file has an empty layout named `SIDEBUTTONS` which could be used for this purpose.)_
- A table to display the search results.
- An image (`Carpark.png`) displayed on the UI.
- A title "Collyers Car Park".

## Development Notes

- The UI is designed using Qt Designer, and the layout is saved in `carpark.ui`.
- `ui.py` is the Python code generated from `carpark.ui` using the `pyuic5` tool. If you make changes to `carpark.ui` with Qt Designer, you will need to regenerate `ui.py` by running the following command in your terminal:
  ```bash
  pyuic5 -x carpark.ui -o ui.py
  ```
- The application connects to an SQLite database named `carpark.db`. Ensure this file is correctly set up with the `Carpark` table and its columns for the application to function as expected.
