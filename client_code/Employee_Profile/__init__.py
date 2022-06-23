from ._anvil_designer import Employee_ProfileTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Globals



class Employee_Profile(Employee_ProfileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.employee_profile_picture.source = app_tables.employee.get(user=anvil.server.call('get_user'))['avatar']
    self.employee_name_tf.text = app_tables.employee.get(user=anvil.server.call('get_user'))['name']
    self.employee_position.text = app_tables.employee.get(user=anvil.server.call('get_user'))['position']
    self.employee_department_dropdown.selected_value = app_tables.employee.get(user=anvil.server.call('get_user'))['department']
    self.employee_department_dropdown.items = [(r['department_name'], r) for r in app_tables.department.search()]
    

    self.repeating_panel_1.items = app_tables.comment.search(comment_to=app_tables.employee.get(user=anvil.server.call('get_user'))['name'])


  def logout_btn_click(self, **event_args):
    logged_in_user = anvil.users.logout()
    open_form('Index')
    pass

  def employee_name_tf_change(self, **event_args):
    Globals.logged_in_user['name'] = self.employee_name_tf.text
    pass

  def employee_position_change(self, **event_args):
    Globals.logged_in_user['position'] = self.employee_position.text
    pass

  def employee_department_dropdown_change(self, **event_args):
    Globals.logged_in_user['department'] = self.employee_department_dropdown.selected_value
    pass

  def employees_list_nav_link_click(self, **event_args):
    open_form('Employees_List')
    pass

  def profile_nav_link_click(self, **event_args):
    pass

  def link_1_click(self, **event_args):
    open_form('Index')
    pass


  







