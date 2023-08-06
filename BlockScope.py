# Block Scope
# BlockScope variable is defined within a for a loop
# however, it is accessible outside the for loop in immediate scope

for i in range(1,10):
    GlobalScope = i
  
def ScopeFunc():
  print(f"GlobalScope: {GlobalScope}")
  for i in range(1,10):
    BlockScope = i
  return BlockScope

Ret = ScopeFunc()
print(f"Returned Value From Func: {Ret}")
