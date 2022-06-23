from ._anvil_designer import Employees_ListTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Employees_List(Employees_ListTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = anvil.server.call('dep_list')
    
  def logout_btn_click(self, **event_args):
    anvil.users.logout()
    open_form('Index')
    pass

  def employees_list_nav_link_click(self, **event_args):
    open_form('Employees_List')
    pass

  def profile_nav_link_click(self, **event_args):
    pass

  def index_link_click(self, **event_args):
    open_form('Index')
    pass

