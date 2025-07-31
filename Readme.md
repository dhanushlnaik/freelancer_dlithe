# DLithe Placement Training Freelancer Tracker

## Context

This project was developed as part of the **DLithe Placement Training Program** for engineering students. The platform aims to simplify the management, allocation, and tracking of student volunteers or freelancers during placement training and recruitment drives. Developed using Python and SQLite, the tracker equips coordinators and placement officers to efficiently allocate tasks, check real-time availability, and maintain updated profiles of all volunteers.

## Table of Contents

- [Project Context](#context)
- [Motivation](#motivation)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Sample Output](#sample-output)
- [Team Members](#team-members)
- [Training Dates](#training-dates)
- [Documentation Outline](#documentation-outline)
- [Contribution Guidelines](#contribution-guidelines)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Motivation

Managing multiple student resources during placement training can quickly become complex without an automated solution. Our tracker centralizes this effort, minimizes manual error, and empowers training coordinators with a simple, reliable CLI interface. It was inspired by real campus needs during the DLithe Placement Training in July 2025.

## Technology Stack

- **Programming Language:** Python 3.x
- **Database:** SQLite (via built-in `sqlite3`)
- **User Interface:** Command-Line Interface
- **Platform:** Cross-platform (Windows, macOS, Linux terminal)

## Features

- **Add New Freelancers** with their name and skills.
- **Display All Freelancers** in a user-friendly table with availability info.
- **Filter by Skill or Availability** for precise volunteer selection.
- **Book or Release** freelancers for key placement roles.
- **Edit Skills:** Update skill sets as trainees gain new expertise.
- **Delete Freelancer** entries safely by ID.
- **Robust Error Handling:** Prevents invalid bookings or actions.
- **Persistent Storage:** All data is saved in a local SQLite database for reliability.

## Installation

1. **Clone this repository** or download all source files into a folder.
2. Ensure **Python 3.x** is installed on your system (`python --version`).
3. No external dependencies required (uses Python’s built-in `sqlite3`).
4. Run the main script:
    ```sh
    python freelancer_tracker.py
    ```

## Usage

Follow the on-screen menu to add, update, filter, book, or release freelancers. All records persist in `freelancers.db`.

**Example menu:**
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

| Column        | Type    | Description                      |
|---------------|---------|----------------------------------|
| id            | INTEGER | Primary Key (auto-increment)     |
| name          | TEXT    | Freelancer’s name                |
| skills        | TEXT    | Comma-separated list of skills   |
| is_available  | INTEGER | 1 = available, 0 = booked        |

## Architecture

![System Architecture](https://github.com/dhanushlnaik/freelancer_dlithe/blob/main/assets/architecture.jpg?raw=true "System Architecture")

## Sample Output

```
==== Freelancer Tracker ====
1. Add Freelancer
2. List All Freelancers
...

ID   Name                 Skills                      Status
--------------------------------------------------------------
1    Aarav Mehta          Python, SQL, ML             Available
2    Riya Singh           Java, Web, Communication    Booked
```

## Team Members

| Name                    | USN         |
|-------------------------|-------------|
| Dhanush Lokesh Naik     | nnm22is044  |
| Parikshith Bhargav K R  | nnm22is109  |
| Tejas M Naik            | nnm23cs513  |
| Vamshikrishna Murali    | nnm22cc066  |

## Training Dates

- **Placement Training Kickoff:**  15th July 2025
- **Project Demo / Submission:**  31st July 2025

## Documentation Outline

1. **Objectives & Context**  
   - Background and motivation.
2. **System Design**  
   - Database schema, logical workflow, key functions.
3. **Code Structure**  
   - CLI flow, modularization, and data handling.
4. **Sample Use Cases & Testing**  
   - Demonstrations, boundary test cases.
5. **Team & Contributions**  
   - Members, roles, and acknowledgments.

## Contribution Guidelines

- Fork the repo and create a feature or bugfix branch.
- Write clear, well-documented code and follow project structure.
- Raise a pull request for review and merging.

## Acknowledgments

- **DLithe** for providing the training platform and project guidance.
- Our faculty coordinators, for feedback and support.
- All participants and stakeholders involved in placement training 2025.

## License

This project is for academic use as part of the DLithe Placement Training Program (July 2025).

**For queries, contact:** _dhanushlnaik@gmail.com_
