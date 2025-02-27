import random as r
nonames = 200
Value = "["
for c in range(nonames - 1):
    Value = Value + f"'Steve-{c}', "
Value = Value + "'Steve-200']"
print(Value)
