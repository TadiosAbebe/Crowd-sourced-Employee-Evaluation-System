from ._anvil_designer import Single_employeeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import Globals

class Single_employee(Single_employeeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def employee_profile_link_click(self, **event_args):
    Globals.employee_name_check = self.item['name']
    open_form('Employee_Profile_user_view')
    pass

  def image_1_mouse_up(self, x, y, button, **event_args):
    Globals.employee_name_check = self.item['name']
    open_form('Employee_Profile_user_view')
    pass




