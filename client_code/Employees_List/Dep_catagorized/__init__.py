from ._anvil_designer import Dep_catagorizedTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Dep_catagorized(Dep_catagorizedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.employee_list.items = anvil.server.call('get_employees_in_dep',self.item)
