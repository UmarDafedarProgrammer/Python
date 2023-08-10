class User:
  def __init__(self):
    print("Constructor is called")
    self.user = "default"


user_1 = User()
user_1.id = 10
user_1.username =  "Angela"

print(user_1.username, user_1.id)
print(user_1.user)
