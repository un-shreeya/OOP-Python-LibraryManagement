# Library Management System (Complete Python OOP Project)
----------------------------------------------------------

Description:
-------------
A command-line Library Management application built in Python using Object-Oriented Programming (OOP).
This program is menu-driven and demonstrates practical use of classes, inheritance, encapsulation, and basic reporting for library items and members.

--------------
  FEATURES:
--------------

Library Item Management:
---------------------------
- Add new books with title, price, and author.
- Add special edition books with edition type.
- Add magazines with title, price, and issue date/month.
- View all library items with details (type, title, author/issue, price).

Member Management:
------------------
- Register new library members with name and member ID.
- View all registered members.

Reports:
---------
- Show total count of library items.
- Show total count of members.

Code Structure:
---------------
- LibraryItem (abstract class): Base for all items, handles price, title, and item count.
- Book, SpecialEdition, Magazine: Inherit from LibraryItem, add specific attributes and display logic.
- Member: Handles member data and member count.
- Main Menu Loop: Provides user interaction for managing items, members, and viewing reports.

Getting Started (Prerequisites)
--------------------------------
- Python 3.7+

Run:
----
python LibraryManagement.py

Note:
------
- All prices must be entered as numbers (e.g., 499.99).
- Editions and issues can be any string (e.g., "First Edition", "June 2025").

Author
-------
Shreeya
