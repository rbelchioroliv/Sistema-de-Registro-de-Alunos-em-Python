# Student Registration System

A simple desktop application developed in Python using Tkinter for managing student records.  
It allows users to add, search, update, and delete student information, including uploading and displaying student photos.

---

## Features

- Add new student records with fields: Name, Email, Phone, Gender, Birth Date, Address, Course, and Photo.
- Search for students by ID and display their details.
- Update existing student records.
- Delete student records.
- Upload and display student photos.
- Display all students in a scrollable table.
- User-friendly GUI with styled widgets using the `clam` theme.

---

## Installation

1. Clone this repository:
git clone https://github.com/seu-usuario/student-registration-system.git
cd student-registration-system

2. Create and activate a virtual environment (recommended):
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

## Usage
Run the main application file:
python your_main_file.py
Replace your_main_file.py with the actual main script filename.

## Project Structure
student-registration-system/
│
├── pictures/                # Images used in the project (logos, icons)
├── main.py                  # Module containing database logic (e.g. registration_system)
├── your_main_file.py        # Main Tkinter application file with GUI
├── requirements.txt         # Python dependencies
└── README.md                # This file


## Notes
Ensure the images used in your code exist in the pictures folder.

The main.py module should provide functions like register_student, search_student, update_student, and delete_student.

The project is intended for local use with a GUI interface.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
