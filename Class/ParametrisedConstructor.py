class User:

  def __init__(self,id):
    print("Parameterised constructor is called")
    self.id = id

user_1 = User(10)
user_1.username =  "Angela"
print(user_1.username, user_1.id)
