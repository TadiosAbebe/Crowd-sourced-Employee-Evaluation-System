from ._anvil_designer import page3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class page3(page3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = app_tables.roles.search()
    self.repeating_panel_1.set_event_handler('x-refresh-roles', self.refresh_roles)

  def refresh_roles(self, **event_args):
    self.repeating_panel_1.items = anvil.server.call('role_list')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('add_role',
                     role_name = self.text_box_1.text
                     )
    self.repeating_panel_1.items = app_tables.roles.search()
    pass
