from estate_track import members, payments, storage, diary


def show_menu():
    print("\n===== The Estate Union Dues Tracker =====")
    print("1. Add a new member")
    print("2. Record a payment")
    print("3. See who has paid / who is owing for a month")
    print("4. See one member's full payment history")
    print("5. List all members")
    print("6. Backup the records")
    print("7. Import members from a file")
    print("8. Quit")


def import_members_from_file(data, filename="new_members.txt"):
    """
    Read member names from a text file, one name per line.
    Some lines might be blank or nonsense on purpose -- we skip those
    politely instead of letting the whole program crash.
    """
    added_count = 0
    skipped_count = 0

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Could not find a file called {filename}.")
        return

    for line in lines:
        name = line.strip()

        if name == "":
            skipped_count += 1
            continue

        # Split the line into at most 3 parts: name, phone, and address
        parts = line.split(",", maxsplit=2)

        name = parts[0].strip()
        phone = parts[1].strip()
        address = parts[2].strip()

        was_added = members.add_member(data, name, phone, address)
        if was_added:
            added_count += 1

    print(f"\nImport finished. Added {added_count} member(s), skipped {skipped_count} bad line(s).")


def main():
    data = storage.load_data()

    while True:
        show_menu()
        choice = input("Choose an option (1-8): ")

        if choice == "1":
            name = input("Enter the new member's name: ")
            phone = input("Enter phone number: ")
            address = input("Enter the new member's address: ")
            members.add_member(data, name, phone, address)
            storage.save_data(data)

        elif choice == "2":
            name = input("Who is paying? ")
            if not members.member_exists(data, name):
                print(f"{name} is not a registered member yet. Please add them first.")
                continue

            try:
                amount = float(input("How much did they pay? "))
            except ValueError:
                print("That doesn't look like a valid amount. Please try again.")
                continue

            month = input("Which month is this payment for? ")
            month.title
            payments.record_payment(data, name, amount, month)
            storage.save_data(data)

        elif choice == "3":
            month = input("Which month do you want to check? ")
            paid, owing = payments.who_has_paid(data, month)

            print(f"\n--- Report for {month} ---")
            print("Paid:")
            if paid:
                for name in paid:
                    print(f"  - {name}")
            else:
                print("  (no payments have been received yet)")

            print("Still owing:")
            if owing:
                for name in owing:
                    print(f"  - {name}")
            else:
                print("  (nobody -- everyone has paid!)")

        elif choice == "4":
            name = input("Whose payment history do you want to see? ")
            history = payments.get_member_history(data, name)

            if not history:
                print(f"No payments found for {name.title()}.")
            else:
                print(f"\n--- Payment history for {name.title()} ---")
                for record in history:
                    print(f"  {record['month']}: {record['amount']} (recorded {record['date_recorded']})")

        elif choice == "5":
            members.list_members(data)

        elif choice == "6":
            storage.backup_data()

        elif choice == "7":
            import_members_from_file(data)
            storage.save_data(data)

        elif choice == "8":
            print("Goodbye, Chairman. Everything has been saved.")
            break

        else:
            print("Please choose a number between 1 and 8.")

if __name__ == "__main__":
    main()
