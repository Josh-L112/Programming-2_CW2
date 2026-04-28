# Programming-2 CW2

## Overview
UniScheduler is a resource booking system developed in Python using Object-Oriented Programming (OOP). The system allows users to book university resources such as meeting rooms and computer labs while preventing scheduling conflicts and ensuring capacity limits are respected.

The application includes both a command-line interface (CLI) and a graphical user interface (GUI) built with Tkinter to improve usability.

---

## Features
- Create bookings for rooms and lab spaces  
- View all existing bookings  
- Conflict detection to prevent double bookings  
- Capacity validation to ensure room limits are not exceeded  
- Persistent data storage using JSON  
- Simple GUI interface using Tkinter  
- Error handling to prevent crashes  

---

## How to Run

### GUI Version (Recommended)
Run the graphical interface:
python main_gui.py

### CLI Version
Run the command-line version:
python main.py

---

## Project Structure

UniScheduler/

│
├── main.py              # CLI version of the system  
├── main_gui.py          # GUI version using Tkinter  
├── scheduler.py         # Handles booking logic and validation  
├── resource.py          # Resource classes (OOP structure)  
├── booking.py           # Booking class  
├── file_handler.py      # Handles JSON file loading/saving  
│
├── bookings.json        # Stores booking data  
│
├── README.md  
└── docs/                # Documentation (UML, report, screenshots) 

---

## Object-Oriented Programming Concepts

The system demonstrates key OOP principles:

- Inheritance  
  A base Resource class is extended by LabSpace and MeetingRoom  

- Encapsulation  
  Data is stored within classes and accessed through methods  

- Polymorphism  
  Methods such as get_details() behave differently depending on the object type  

---

## Core Functionality

The system works by allowing users to enter booking details including resource, time, and number of people. It then performs checks before saving the booking:

- Checks if the room is already booked at the same time  
- Checks if the room can handle the requested capacity  
- Saves valid bookings to a JSON file  

---

## Data Storage

- All bookings are stored in bookings.json  
- Data is loaded when the program starts  
- Data is saved when the program exits  
- If the file is missing, the system creates a new one automatically  

---

## Error Handling

The system includes basic defensive programming:

- Handles invalid input (e.g. text instead of numbers)  
- Prevents crashes using try/except blocks  
- Displays error messages for incorrect entries  

---

## Limitations

- Uses JSON instead of a database  
- GUI is simple and not fully styled  
- Does not support advanced features like recurring bookings  

---

## Future Improvements

- Add a graphical calendar view  
- Replace JSON with a database (e.g. SQLite)  
- Implement user login/authentication  
- Improve GUI layout and design  
- Add search and filtering features  

---

## Authors

- Tomas Striska  
- Joshua Lemaire 

---

## Notes

This project was developed as part of a university coursework assignment focusing on Object-Oriented Programming, system design, and usability principles.