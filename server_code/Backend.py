import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime


@anvil.server.callable
def verify_user():
  logged_in_user = anvil.users.get_user()
  if logged_in_user['role'] == None:
    return "newAdmin"
  elif logged_in_user['role']['role'] == 'Employee':
    return "Employee_Profile"
  elif logged_in_user['role']['role'] == 'Client':
    return "Employees_List"
  elif logged_in_user['role']['role'] == 'Admin':
    return "newAdmin"
  else:
    return "Uknown Error"
  
@anvil.server.callable
def get_user():
  return anvil.users.get_user(allow_remembered=False)

@anvil.server.callable
def get_employees():
  return app_tables.employee.search(tables.order_by("added", ascending=False))

@anvil.server.callable
def get_client():
  return app_tables.clients.search(tables.order_by("added", ascending=False))

@anvil.server.callable
def get_employees_in_dep(department):
  return app_tables.employee.search(department=department)

@anvil.server.callable
def dep_list():
  return app_tables.department.search()

@anvil.server.callable
def role_list():
  return app_tables.roles.search()

@anvil.server.callable
def user_list():
  return app_tables.users.search()

@anvil.server.callable
def add_employee(user, name, position, avatar, bio, department):
  app_tables.employee.add_row(user=user, name= name, position=position, avatar=avatar, bio=bio, department=department, added=datetime.now())
  
@anvil.server.callable
def add_client(user, name):
  app_tables.clients.add_row(user=user, name=name, added=datetime.now())
  
@anvil.server.callable
def add_dep(dep_name):
  app_tables.department.add_row(department_name=dep_name)
  
@anvil.server.callable
def add_role(role_name):
  app_tables.roles.add_row(role=role_name)
  
@anvil.server.callable
def mod_user(user, enable, role):
  i = app_tables.users.get(email=user)
  i['enabled'] = enable
  i['role'] = role 

@anvil.server.callable
def mod_user2(user, role):
  i = app_tables.users.get(email=user)
  i['role'] = role 
  
@anvil.server.callable
def delete_employee(employee):
  employee.delete()
  
@anvil.server.callable
def delet_dep(dep):
  dep.delete()
  
@anvil.server.callable
def delet_role(role):
  role.delete()
  
@anvil.server.callable
def delet_user(user):
  user.delete()
  
@anvil.server.callable
def delet_client(client):
  client.delete()
  