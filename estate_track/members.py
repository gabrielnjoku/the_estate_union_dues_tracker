from . import diary


def add_member(data, name):
    """
    Add a new member's name to the records, unless they're already there.
    'data' is the whole records dictionary (holding members + payments).
    Returns True if the member was added, False if they already existed.
    """
    name = name.strip().title()
    if name in data["members"]:
        print(f"{name} is already a registered member.")
        return False

    data["members"].append(name)
    diary.write_entry(f"New member added: {name}")
    print(f"{name} has been added as a new member.")
    return True


def member_exists(data, name):
    """Return True if this name is already a registered member."""
    name = name.strip().title()
    return name in data["members"]


def list_members(data):
    """Print every registered member's name."""
    if not data["members"]:
        print("No members have been added yet.")
        return

    print("\n--- All Members ---")
    for name in data["members"]:
        print(f"- {name}")
