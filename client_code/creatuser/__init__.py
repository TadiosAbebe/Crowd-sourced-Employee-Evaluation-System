from ._anvil_designer import creatuserTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class creatuser(creatuserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.drop_down_1.items = [(r['role'],r) for r in app_tables.roles.search()]

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.signup_with_email(
      self.user.text,
      self.password.text
    )
    
    anvil.server.call(
      'mod_user', 
      user = self.user.text,
      enable = self.check_box_1.checked, 
      role = self.drop_down_1.selected_value
    )
    pass

