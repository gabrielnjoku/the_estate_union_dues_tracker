from datetime import datetime
from . import diary


def add_member(data, name, phone, address):
    """
    Add a new member's name to the records, unless they're already there.
    'data' is the whole records dictionary (holding members + payments).
    Returns True if the member was added, False if they already existed.
    """
    name = name.strip().title()    
    member_details = {
        "name": name,
        "phone": phone,
        "address": address,
        "date_registered": datetime.now().strftime("%Y-%m-%d"),
    }
    for member in data["members"]:
        if member["name"] == name:
            return False
        
    data["members"].append(member_details)

    diary.write_entry(f"New member added: {name}")
    print(f"{name} has been added as a new member.")
    return True


def member_exists(data, name):
    """Return True if this name is already a registered member."""
    name = name.strip().title()
    for member in data["members"]:
        if member["name"] == name:
            return True        
    return False


def list_members(data):
    """Print every registered member's name."""
    if not data["members"]:
        print("No members have been added yet.")
        return

    print("\n-------- All Members --------")
    print("\nMember Fullname \t Phone No \t Address \t Created")
    for member in data["members"]:
        print(f"{member["name"]} \t\t {member["phone"]} \t {member["address"]} \t\t {member["date_registered"]}")
    
