from Demo_line.box import Box
from Demo_line.sql_tools import execute_request, request

box = Box(3, 1)

print(execute_request(box.database, request('SELECT', '*', 'portal', 'id = 2')))
print('*******************')

print(execute_request(box.database, request('SELECT', '*', 'portal')))
