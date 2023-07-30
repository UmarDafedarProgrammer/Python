def add(n1,n2):
  """Addition takes two numbers as an inputs"""
  return n1+n2

def subtract(n1,n2):
  """Subtraction takes two numbers as an inputs"""
  return n1-n2

def multiply(n1,n2):
  """Multiplication takes two numbers as an inputs"""
  return n1*n2

def divide(n1,n2):
  """Divison takes two numbers as an inputs"""
  return n1/n2

Operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

num1 = int(input("Please, Enter the first number?: "))
ops = input("Enter the operation, you want to perform: ")
num2 = int(input("Please, Enter the Second number?:  "))
print(Operations[ops](num1,num2))
