import os
from datetime import datetime

JOURNAL_FILE = "journal.txt"

def load_entries():
    if not os.path.exists(JOURNAL_FILE):
        open(JOURNAL_FILE, 'w').close()  # Create file if missing
        return []
    with open(JOURNAL_FILE, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n\n')
        return [entry for entry in lines if entry.strip()]

def save_entries(entries):
    with open(JOURNAL_FILE, 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(entries))

def view_entries(entries):
    if not entries:
        print("No journal entries found.")
        return
    for i, entry in enumerate(entries, 1):
        print(f"\nEntry {i}:\n{entry}\n" + "-"*40)

def add_entry(entries):
    print("Write your journal entry (type DONE on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'DONE':
            break
        lines.append(line)
    content = '\n'.join(lines).strip()
    if not content:
        print("Empty entry not added.")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entries.append(f"{timestamp}\n{content}")
    save_entries(entries)
    print("Entry added successfully!")

def remove_entry(entries):
    view_entries(entries)
    if not entries:
        return
    try:
        index = int(input("Enter the number of the entry to delete: "))
        if 1 <= index <= len(entries):
            entries.pop(index - 1)
            save_entries(entries)
            print("Entry deleted successfully.")
        else:
            print("Error: Entry number out of range.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    entries = load_entries()
    while True:
        print("\nJournal Menu:")
        print("1. View Journal Entries")
        print("2. Add a New Entry")
        print("3. Remove an Entry")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            view_entries(entries)
        elif choice == '2':
            add_entry(entries)
        elif choice == '3':
            remove_entry(entries)
        elif choice == '4':
            print("Exiting... Your journal is saved.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
