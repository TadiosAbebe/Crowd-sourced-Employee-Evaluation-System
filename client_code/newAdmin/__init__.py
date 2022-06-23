from ._anvil_designer import newAdminTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..page1 import page1
from ..page2 import page2
from ..page3 import page3
from ..page4 import page4
from ..page5 import page5

class newAdmin(newAdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.link_1.tag.form_to_open = page1()
    self.link_2.tag.form_to_open = page2()
    self.link_3.tag.form_to_open = page3()
    self.link_4.tag.form_to_open = page4()
    self.link_5.tag.form_to_open = page5()

  def nav_link_click(self, **event_args):
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    self.reset_links()
    event_args['sender'].role = 'selected'
    form_to_open = event_args['sender'].tag.form_to_open

    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)


  def reset_links(self, **event_args):
    self.link_1.role = ''
    self.link_2.role = ''
    self.link_3.role = ''
    self.link_4.role = ''
    self.link_5.role = ''

  def index_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Index')
    pass

