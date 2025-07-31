# Placement Training Freelancer Tracker

## Overview

This project is a **Freelancer Tracker** application designed to streamline the management, booking, and tracking of freelancers available for placement training. The system allows users to add freelancers, list their details, filter by skills and availability, book or release freelancers, update their skills, and manage the database via a user-friendly Command Line Interface (CLI).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Team Members](#team-members)
- [Training Dates](#training-dates)
- [Documentation](#documentation)

## Features

- **Add Freelancers** with their name and skill set
- **List All Freelancers** in a tabular format
- **Filter Freelancers** by skill and availability
- **Book** or **Release** (mark as available) freelancers
- **Edit Skills** or **Delete** freelancer entries
- **Error Handling** for invalid actions and inputs
- **Persistent SQLite Database** backend

## Installation

1. **Clone the repository** or download the source code.
2. Ensure you have Python 3.x installed.
3. Required library: `sqlite3` (comes standard with Python).
4. Run the program:
   ```
   python freelancer_tracker.py
   ```

## Usage

Follow the on-screen menu to manage freelancers:
- Add, list, filter, book, release, edit, or delete freelancer entries.
- When filtering, you can search for specific skills (e.g., Python, Java).
- Booking a freelancer marks them as unavailable until they are released.

**Sample CLI Menu:**
```
==== Freelancer Tracker ====
1. Add Freelancer
2. List All Freelancers
3. Filter Freelancers by Skill / Availability
4. Book a Freelancer
5. Mark Freelancer as Available
6. Delete Freelancer
7. Update Freelancer Skills
8. Exit
```

## Database Schema

**Table `freelancers`:**
| Column        | Type       | Description                 |
|---------------|------------|-----------------------------|
| id            | INTEGER    | Primary Key (auto-increment)|
| name          | TEXT       | Freelancer’s name           |
| skills        | TEXT       | Comma-separated skills      |
| is_available  | INTEGER    | 1 = available, 0 = booked   |

## Team Members

| Name                     | USN           |
|--------------------------|---------------|
| Dhanush Lokesh Naik      | nnm22is044    |
| Parikshith Bhargav K R   | nnm22is109    |
| Tejas M Naik             | nnm23cs513    |
| Vamshikrishna Murali     | nnm22cc066    |

## Training Dates

- **Placement Training Kickoff:**  15th July 2025
- **Project Demo / Submission:**  31st July 2025


## Documentation

1. **System Design**
   - ER diagram and schema explanation
2. **Core Application Logic**
   - CLI structure, error handling, and modularization
3. **Features**
   - Description of each program feature and user story
4. **Testing & Quality Assurance**
   - Example test cases or usage scenarios
5. **How to Contribute**
   - [Optional if open-source] Fork the repository, raise a PR

## License

This project is for academic and placement training purposes.