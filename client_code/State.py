import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
user_email = [(r['email'], r) for r in app_tables.users.search()]
depart = [(r['department_name'], r) for r in app_tables.department.search()]