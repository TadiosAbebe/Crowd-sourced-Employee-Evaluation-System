from ._anvil_designer import page5Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class page5(page5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.client_list.items = anvil.server.call('get_client')
    self.drop_down_1.items = [(r['email'], r) for r in app_tables.users.search()]
    self.client_list.set_event_handler('x-refresh-client', self.refresh_client)

    
  def refresh_client(self, **event_args):
    self.client_list.items = anvil.server.call('get_client')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call(
      'add_client',
      user = self.drop_down_1.selected_value,
      name = self.text_box_1.text,
    )
    self.client_list.items = anvil.server.call('get_client')

    pass


