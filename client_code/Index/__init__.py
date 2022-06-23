from ._anvil_designer import IndexTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Index(IndexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    anvil.users.logout()
    
    
  def signin_btn_click(self, **event_args):
    anvil.users.login_with_form()
    open_form(anvil.server.call('verify_user'))
    pass

  def signup_btn_click(self, **event_args):
    anvil.users.signup_with_form()
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('newAdmin')
    pass





