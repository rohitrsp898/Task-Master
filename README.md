# Task-Master
Task master is simple Task adder in to SQLlite database using Python and Flask framework.

Main code file is app.py with Templates in tempplates folder.

In requirements.txt all the required packages are mentioned with there version.

test.db is SQLalchemy data base to store the Tasks.

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

db=SQLAlchemy(app)

To created database run the cmd in the same folder as app.py
>>> from app import db

>>> db.create_all()

>>> exit()

Here app is your python file name and db is variable for database.
