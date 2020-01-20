# security.py

from werkzeug.security import safe_str_cmp
from user import User  #importing a user object from user.py

users = [
   User(1, 'rolf', 'abcd')   #username : rolf and password : abcd
]

username_mapping = {u.username: u for u in users} #assign key mapping pairs
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
   user = username_mapping.get(username, None)
   if user and safe_str_cmp(user.password ,password):
    return user
def identity(payload):
   user_id = payload['identity']
   return userid_mapping.get(user_id, None)

