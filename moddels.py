from piccolo.table import Table
from piccolo.columns import Varchar, Email

class User(Table):
    name = Varchar(length=100)
    email = Email(unique=True)
