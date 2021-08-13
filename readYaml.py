import yaml

yaml_file = open("walkmeOps.yaml")
parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
print(parsed_yaml_file.get("zipFileName"))
print(parsed_yaml_file.get("operation"))