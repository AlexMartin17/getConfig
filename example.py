from getConfig import getVariable

#Lets calculate perimeter of a triangle

#Getting values from config file
configFile = "config.cfg"

#getVariable usage - getVariable(configfile, variable name)

a = getVariable(configFile, "configX")
b = getVariable(configFile, "configY")
c = getVariable(configFile, "configZ")

p = eval(a) + eval(b) + eval(c)

print(f"Perimeter of a triangle with edges A = {a},B = {b},C = {c}, is P = {p}")
