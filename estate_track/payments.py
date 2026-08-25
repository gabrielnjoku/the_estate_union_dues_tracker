from datetime import datetime

from estate_track import diary


def record_payment(data, name, amount, month):
    """
    Save a payment: who paid, how much, and for which month.
    'data' is the whole records dictionary.
    """
    name = name.strip().title()
    month = month.strip().title()
    payment = {
        "name": name,
        "amount": amount,
        "month": month,
        "date_recorded": datetime.now().strftime("%Y-%m-%d"),
    }
    data["payments"].append(payment)

    diary.write_entry(f"Payment recorded: {name} paid {amount} for {month}")
    print(f"Recorded: {name} paid {amount} for {month}.")


def get_member_history(data, name):
    """Return a list of every payment made by one specific member."""    
    name = name.strip().title()
    history = []
    for payment in data["payments"]:
        if payment["name"] == name:
            history.append(payment)
    return history


def who_has_paid(data, month):
    """
    Look through all members and figure out who has paid for a given
    month, and who is still owing.
    Returns two lists: (paid_names, owing_names)
    """
    month = month.strip().title()
    paid_names = []
    for payment in data["payments"]:
        if payment["month"] == month:
            if payment["name"] not in paid_names:
                paid_names.append(payment["name"])

    owing_names = []
    for member in data["members"]:
        if member["name"] not in paid_names:
            owing_names.append(member["name"])

    return paid_names, owing_names
