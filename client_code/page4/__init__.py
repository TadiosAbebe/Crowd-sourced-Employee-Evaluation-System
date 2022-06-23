from ._anvil_designer import page4Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class page4(page4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = app_tables.users.search()
    self.repeating_panel_1.set_event_handler('x-refresh-user', self.refresh_user)
    
    self.drop_down_1.items = [(r['role'],r) for r in app_tables.roles.search()]

  def refresh_user(self, **event_args):
    self.repeating_panel_1.items = anvil.server.call('user_list')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.signup_with_email(
      self.user.text,
      self.password.text
    )
    anvil.server.call(
      'mod_user2', 
      user = self.user.text,
      role = self.drop_down_1.selected_value
    )
    self.user.text = ""
    self.password.text = ""
    self.check_box_1.checked = False
    self.repeating_panel_1.items = app_tables.users.search()
    pass

