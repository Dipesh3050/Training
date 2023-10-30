
#importing modules
import mymodule

a = mymodule.person1["age"]
print(a)

#Python Dates
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#python json
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
print(y)

#python pip
import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

#This method capitalizes the first letter of each word.
