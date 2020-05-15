import re
import json

def getVariable(file, type, var):
    value = None
    try:
        with open(file) as configFile:
            if type == "cfg" or type == "INI" or type == "ini":
                for line in configFile:
                    line = line.strip()
                    if line.startswith(f"{var}="):
                        value = re.sub(f"{var}=","",line)
            elif type == "XML" or type == "xml":
                for line in configFile:
                    line = line.strip()
                    if line.startswith(f"<{var}>") and line.endswith(f"</{var}>"):
                        value = re.sub(f"<{var}>","",line)
                        value = re.sub(f"</{var}>","",value)
            elif type == "JSON" or type == "json":
                data = json.load(configFile)
                for record in data['configfile']:
                    value = record[f'{var}']
            else:
                raise Exception(f"Unsupported file type - {type}!")
        if value == None:
            raise Exception(f"{var} not found in config file!")
        else:
            return(value)
    except FileNotFoundError:
        print(f"{file} not found, make sure that the path is correct.")
