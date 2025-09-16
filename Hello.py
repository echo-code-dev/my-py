print("hello python")
print("just trying out git")
values = range(0, 10, 2)
for value in values:
  if values.index(value) == len(values) - 1:
    print(value)
  else:
    print(value, end=', ')
print("this is version 4")