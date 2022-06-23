from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


# Global variables
employee_name_check = None
user_form = app_tables.employee.get(user=anvil.server.call('get_user'))
