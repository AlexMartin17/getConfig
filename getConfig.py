import re
def getVariable(file, var):
    try:
        with open(file) as configFile:
            for line in configFile:
                line = line.strip()
                if line.startswith(f"{var}="):
                    value = re.sub(f"{var}=","",line)
        return(value)
    except FileNotFoundError:
        print(f"{file} not found, make sure that the path is correct.")
