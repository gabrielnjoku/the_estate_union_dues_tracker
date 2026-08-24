from datetime import datetime

DIARY_FILE = "audit_trail.txt"


def write_entry(event_description):
    """
    Add one line to the BOTTOM of the diary file.

    We open the file using "a" (append) mode instead of "w" (write)
    mode. Append mode adds new text to the end of the file without
    erasing anything that was already there.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DIARY_FILE, "a") as file:
        file.write(f"[{timestamp}] {event_description}\n")
