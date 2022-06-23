from ._anvil_designer import page2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class page2(page2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = app_tables.department.search()
    self.repeating_panel_1.set_event_handler('x-refresh-departments', self.refresh_departments)
    
  def refresh_departments(self, **event_args):
    self.repeating_panel_1.items = anvil.server.call('dep_list')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('add_dep',
                     dep_name = self.text_box_1.text
                     )
    self.repeating_panel_1.items = app_tables.department.search()
    pass

