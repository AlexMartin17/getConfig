from getConfig import getVariable

#Lets calculate perimeter of a triangle

#Getting values from config file
configFile = "config.cfg"

#getVariable usage - getVariable(configfile, type, variable name)

a = getVariable(configFile, "cfg", "configX")
b = getVariable(configFile, "cfg", "configY")
c = getVariable(configFile, "cfg", "configZ")

p = eval(a) + eval(b) + eval(c)

print(f"Perimeter of a triangle with edges A = {a},B = {b},C = {c}, is P = {p}")

#Getting values from .INI file
configFile = "config.ini"

a = getVariable(configFile, "INI", "configX")
b = getVariable(configFile, "INI", "configY")
c = getVariable(configFile, "INI", "configZ")

p = eval(a) + eval(b) + eval(c)

print(f"Perimeter of a triangle with edges A = {a},B = {b},C = {c}, is P = {p} (from .INI file)")

#Getting values from .XML file
configFile = "config.xml"

a = getVariable(configFile, "XML", "configX")
b = getVariable(configFile, "XML", "configY")
c = getVariable(configFile, "XML", "configZ")

p = eval(a) + eval(b) + eval(c)

print(f"Perimeter of a triangle with edges A = {a},B = {b},C = {c}, is P = {p} (from .XML file)")

#Getting values from .JSON file
configFile = "config.json"

name = getVariable(configFile, "JSON", "firstName")
lastname = getVariable(configFile, "JSON", "lastName")
age = getVariable(configFile, "JSON", "age")

print(f"Hi my first name is {name}, my last name is {lastname}, and I'm {age} years old!")
