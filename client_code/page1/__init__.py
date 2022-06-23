from ._anvil_designer import page1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class page1(page1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.employees_list.items = anvil.server.call('get_employees')
    self.drop_down_1.items = [(r['email'], r) for r in app_tables.users.search()]
    self.drop_down_2.items = [(r['department_name'], r) for r in app_tables.department.search()]
    self.employees_list.set_event_handler('x-refresh-employees', self.refresh_employees)
    
    self.drop_down_3.items = [(r['role'],r) for r in app_tables.roles.search()]

    
  def refresh_employees(self, **event_args):
    self.employees_list.items = anvil.server.call('get_employees')

    
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

  def button_1_click(self, **event_args):
    anvil.server.call(
      'add_employee',
      user = self.drop_down_1.selected_value,
      name = self.text_box_1.text,
      position = self.text_box_2.text,
      avatar = self.file_loader_1.file,
      bio = self.text_box_3.text,
      department = self.drop_down_2.selected_value
    )
    self.employees_list.items = anvil.server.call('get_employees')
    pass

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def create_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.signup_with_email(
      self.user.text,
      self.password.text,
      remember= False
    )
    anvil.server.call(
      'mod_user2', 
      user = self.user.text,
      role = self.drop_down_3.selected_value
    )
    pass

