import yaml
from datetime import date


yaml_file = open("walkmeOps.yaml")
parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)

file1 = open("Logger.txt","a")
fname= parsed_yaml_file.get("zipFileName")
op= parsed_yaml_file.get("operation")
today = date.today()
product= parsed_yaml_file.get("operation")
L = [f"Date: {today} \t ZipFile: {fname} \t ProductTeam: {product} \t Operation: {op} \n"] 
  
# \n is placed to indicate EOL (End of Line)
file1.writelines(L)
file1.close()