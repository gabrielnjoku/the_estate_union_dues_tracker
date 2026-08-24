import json
from datetime import datetime

DATA_FILE = "data_store.json"


def load_data():
    """
    Try to open the saved data file and read it.
    """
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print("No saved records found yet. Starting a brand new notebook for the estate.")
        return {"members": [], "payments": []}

    except json.JSONDecodeError:
        print("Warning: the saved records file looks damaged or was tampered with.")
        print("Starting fresh so the program can keep working.")
        return {"members": [], "payments": []}


def save_data(data):
    """Write the current data (members and payments) to the file on disk."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def backup_data():
    """
    Bonus feature: make a dated copy of the current records file,
    so the chairman always has a spare copy from a specific date.
    """
    try:
        with open(DATA_FILE, "r") as original_file:
            contents = original_file.read()
    except FileNotFoundError:
        print("There is nothing saved yet, so there is nothing to back up.")
        return

    today_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{today_stamp}.json"

    with open(backup_filename, "w") as backup_file:
        backup_file.write(contents)

    print(f"Backup saved as {backup_filename}")
