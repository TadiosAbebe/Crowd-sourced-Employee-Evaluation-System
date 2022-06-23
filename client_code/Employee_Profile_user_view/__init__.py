from ._anvil_designer import Employee_Profile_user_viewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Globals

class Employee_Profile_user_view(Employee_Profile_user_viewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    logged_in_user = app_tables.employee.get(name=Globals.employee_name_check)
    self.employee_profile_picture.source = logged_in_user['avatar']
    self.employee_name_tf.text = logged_in_user['name']
    self.employee_position.text = logged_in_user['position']
    self.employee_department_dropdown.selected_value = logged_in_user['department']
    self.employee_department_dropdown.items = [(r['department_name'], r) for r in app_tables.department.search()]
    self.repeating_panel_1.items = app_tables.comment.search(comment_to=logged_in_user['name'])
    
    self.rating_value.items = ([("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)])

  def logout_btn_click(self, **event_args):
    anvil.users.logout()
    open_form('Index')
    pass

  def employees_list_nav_link_click(self, **event_args):
    open_form('Employees_List')
    pass

  def profile_nav_link_click(self, **event_args):
    pass
  
  def link_1_click(self, **event_args):
    open_form('Index')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    comment_in = self.text_area_1.text
    commenter_in = anvil.users.get_user()
    comment_to_in = app_tables.employee.get(name=Globals.employee_name_check)

    if commenter_in['role']['role'] == 'employee':
      commenter_row = app_tables.employee.get(user=commenter_in)
      commenter_name = commenter_row['name']

      add_comment = app_tables.comment.add_row(comment_to=comment_to_in['name'],
                                               Comment=comment_in,
                                               Commenter=commenter_name)
    elif commenter_in['role']['role'] == 'client':
      commenter_row = app_tables.clients.get(user=commenter_in)
      commenter_name = commenter_row['name']

      add_comment = app_tables.comment.add_row(comment_to=comment_to_in['name'],
                                               Comment=comment_in,
                                               Commenter=commenter_name)
    elif commenter_in['role']['role'] == 'admin':
      return "Admin_Panel"
    else:
      return "Uknown Error"
    
    logged_in_user = app_tables.employee.get(name=Globals.employee_name_check)
    self.repeating_panel_1.items = app_tables.comment.search(comment_to=logged_in_user['name'])
    self.text_area_1.text = ""
    pass

  def rating_value_change(self, **event_args):
    """This method is called when an item is selected"""
    pass






