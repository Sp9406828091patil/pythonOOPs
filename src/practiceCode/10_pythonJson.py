import json

# x = '[1, 2, 3, 4]'
# x = '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y['name'])


import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(type(x))
print(type(y))

