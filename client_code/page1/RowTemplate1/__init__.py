from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import State

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.drop_down_1.items = State.user_email
    self.drop_down_2.items = State.depart
    self.drop_down_1_copy.items = State.user_email
    self.drop_down_2_copy.items = State.depart

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.write_view.visible = True
    self.read_view.visible = False
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.write_view.visible = False
    self.read_view.visible = True
    self.refresh_data_bindings()
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('delete_employee', self.item)
    self.parent.raise_event('x-refresh-employees')
    pass



