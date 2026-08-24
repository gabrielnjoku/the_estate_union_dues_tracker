The Estate Union Dues Tracker
=============================

What this program does
-----------------------
This program helps the Estate Chairman keep track of estate dues:
- Adding new members
- Recording who paid, how much, and for which month
- Checking who has paid and who is still owing, for any month
- Looking up one member's full payment history

Everything is saved to disk, so closing the program and opening it
again -- even after NEPA takes the light -- never loses any data.

How to start it
----------------
From inside this folder, run:

    python main.py

Only ever run main.py. Everything else works behind the
scenes and is not meant to be run on its own.

What each file does 
-------------------
main.py                  The application entry point. Shows the menu and sends
                          each request to the right file. This is the
                          only file that needs to be run.

estate_track/__init__.py   The sign on the door that tells
                          Python "this folder is a package."

estate_track/members.py    Handles adding new members and checking who
                          is registered.

estate_track/payments.py   Handles recording payments and answering
                          "who has paid" and "member history"
                          questions.

estate_track/storage.py    Handles saving and loading all the data to
                          and from disk (data_store.json), plus
                          making backups.

estate_track/diary.py      Writes a timestamped diary entry (audit_trail.txt)
                          every time something important happens.

Data files created automatically
----------------------------------
data_store.json   The actual saved records (members + payments).
                    Created the first time you add a member or a
                    payment.

audit_trail.txt           A plain-text diary of everything that has ever
                    happened, with dates and times. You can open this
                    with any text editor, even without running the
                    program.

Bonus features
---------------
- Menu option 6 makes a dated backup copy of the records file, named
  something like backup_2026-08-24_14-30-00.json.
- Menu option 7 reads new members from a file called
  new_members.txt (one name per line, placed in this same folder)
  and safely skips any blank or nonsense lines instead of crashing.

If something goes wrong
-------------------------
- FIRST TIME RUNNING: no data file exists yet, so the program simply
  starts fresh, like opening a brand new notebook. This is normal.
- If the saved records file is ever damaged or tampered with, the
  program notices, explains the problem in plain language, and keeps
  working with a fresh set of records -- instead of crashing.
