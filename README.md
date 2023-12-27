# assignment_python
## Explanation of the program
This program can edit and show almost any SQLLite database using the terminal.
The following commands are implemented:
- add: adds a new record to its table
- change: change a record in its table
- export: exports the database to a new csv file this command only fully works when one table of the database references all the other tables
- help: gives the use case of a command and gives its usage
- remove: removes a record from its table
- see: shows a table of the database

## Explanation of the given database
The expenses database consists of two tables.

### Expenses table
Fields:
- name
- amount
- expense_id (Primary key)
- category_id (Foreign key to Categories table)

### Categories table
Fields:
- name
- id (Primary key)
- description

## Configuration
### expenses.db placement
Place the expenses.db file in the db directory

### Settings file
Make a settings.py file with the following code:
```
from os import path
import os

DATABASE_PATH = path.join(os.getcwd(), "db", "expenses.db")
```