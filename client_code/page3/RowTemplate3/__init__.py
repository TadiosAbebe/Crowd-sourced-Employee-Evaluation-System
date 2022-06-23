from ._anvil_designer import RowTemplate3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate3(RowTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.enabled = True
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('delet_role',self.item)
    self.parent.raise_event('x-refresh-roles')
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.enabled = False
    pass
