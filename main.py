import sqlite3

# ---------- DATABASE SETUP ----------
conn = sqlite3.connect("database/freelancers.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS freelancers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    skills TEXT NOT NULL,
    is_available INTEGER DEFAULT 1
)
''')
conn.commit()


# ---------- UTILITY FUNCTIONS ----------
def print_freelancers(rows):
    if not rows:
        print("(No freelancers found)\n")
        return
    print("{:<4} {:<20} {:<30} {:<12}".format('ID', 'Name', 'Skills', 'Status'))
    print("-" * 70)
    for row in rows:
        status = "Available" if row[3] else "Booked"
        print("{:<4} {:<20} {:<30} {:<12}".format(row[0], row[1], row[2], status))
    print()


# ---------- CORE FUNCTIONS ----------
def add_freelancer(name, skills):
    if not name.strip() or not skills.strip():
        print('❌ Name and skills cannot be empty!\n')
        return
    cursor.execute(
        "INSERT INTO freelancers (name, skills, is_available) VALUES (?, ?, 1)",
        (name.strip(), skills.strip()))
    conn.commit()
    print("✅ Freelancer added successfully!\n")

def list_freelancers():
    cursor.execute("SELECT * FROM freelancers")
    rows = cursor.fetchall()
    print_freelancers(rows)

def filter_freelancers(skill=None, available_only=False):
    query = "SELECT * FROM freelancers WHERE 1=1"
    params = []
    if skill:
        # for loose matching
        query += " AND LOWER(skills) LIKE ?"
        params.append(f"%{skill.lower()}%")
    if available_only:
        query += " AND is_available = 1"
    cursor.execute(query, params)
    results = cursor.fetchall()
    print_freelancers(results)

def book_freelancer(freelancer_id):
    # Check if exists and is available
    cursor.execute("SELECT is_available FROM freelancers WHERE id = ?", (freelancer_id,))
    row = cursor.fetchone()
    if not row:
        print("❌ Freelancer ID does not exist.\n")
        return
    if row[0] == 0:
        print("❌ Freelancer is already booked/unavailable.\n")
        return
    cursor.execute("UPDATE freelancers SET is_available = 0 WHERE id = ?", (freelancer_id,))
    conn.commit()
    print(f"📦 Freelancer ID {freelancer_id} booked successfully!\n")

def make_available(freelancer_id):
    cursor.execute("SELECT is_available FROM freelancers WHERE id = ?", (freelancer_id,))
    row = cursor.fetchone()
    if not row:
        print("❌ Freelancer ID does not exist.\n")
        return
    if row[0] == 1:
        print("✅ Freelancer is already available.\n")
        return
    cursor.execute("UPDATE freelancers SET is_available = 1 WHERE id = ?", (freelancer_id,))
    conn.commit()
    print(f"✅ Freelancer ID {freelancer_id} marked as available.\n")

def delete_freelancer(freelancer_id):
    cursor.execute("SELECT id FROM freelancers WHERE id = ?", (freelancer_id,))
    if not cursor.fetchone():
        print("❌ Freelancer ID does not exist.\n")
        return
    cursor.execute("DELETE FROM freelancers WHERE id = ?", (freelancer_id,))
    conn.commit()
    print(f"🗑️  Freelancer ID {freelancer_id} deleted.\n")

def update_skills(freelancer_id, new_skills):
    cursor.execute("SELECT id FROM freelancers WHERE id = ?", (freelancer_id,))
    if not cursor.fetchone():
        print("❌ Freelancer ID does not exist.\n")
        return
    cursor.execute("UPDATE freelancers SET skills = ? WHERE id = ?", (new_skills, freelancer_id))
    conn.commit()
    print(f"📝 Freelancer ID {freelancer_id} skills updated.\n")

# ---------- CLI MENU ----------
def menu():
    while True:
        print("==== Freelancer Tracker ====")
        print("1. Add Freelancer")
        print("2. List All Freelancers")
        print("3. Filter Freelancers by Skill / Availability")
        print("4. Book a Freelancer")
        print("5. Mark Freelancer as Available")
        print("6. Delete Freelancer")
        print("7. Update Freelancer Skills")
        print("8. Exit")
        print()

        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                name = input("Enter name: ")
                skills = input("Enter comma-separated skills: ")
                add_freelancer(name, skills)
            elif choice == "2":
                list_freelancers()
            elif choice == "3":
                skill = input("Enter skill to filter (leave blank for any): ")
                available = input("Available only? (y/n): ").strip().lower() == "y"
                filter_freelancers(skill if skill else None, available)
            elif choice == "4":
                fid = int(input("Enter Freelancer ID to book: "))
                book_freelancer(fid)
            elif choice == "5":
                fid = int(input("Enter Freelancer ID to mark available: "))
                make_available(fid)
            elif choice == "6":
                fid = int(input("Enter Freelancer ID to delete: "))
                delete_freelancer(fid)
            elif choice == "7":
                fid = int(input("Enter Freelancer ID to update skills: "))
                new_skills = input("Enter new comma-separated skills: ")
                update_skills(fid, new_skills)
            elif choice == "8":
                print("Exiting... 👋")
                break
            else:
                print("❌ Invalid choice. Try again.\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
    cursor.close()
    conn.close()

menu()
