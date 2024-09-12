# import os
# # import "sql.py" as sql
# from sql import get_main_strings 

# # print(os.walk("./InterIIT-Website"))
# for i in os.walk("./tmp"):
#     # print("requirements.txt" in i[-1] or "package.json" in i[-1])
#     if "requirements.txt" in i[-1] or "package.json" in i[-1]:
#         print(i[0])
        
# print(get_main_strings())

import os
import json

# subprocess.run(['git','clone','https://github.com/VedantBhosle31/InterIIT-Website.git', 'tmp'])
# os.system("git clone https://github.com/VedantBhosle31/InterIIT-Website.git tmp")
os.system("git clone https://github.com/Python-World/python-mini-projects tmp")

found_files = []

for root,dirs,files in os.walk("./tmp"):
    if "reuirements.txt" in files:
        temp_path = os.path.join(root,"requirements.txt")
        found_files.append(temp_path)
    if "package.json" in files:
        temp_path = os.path.join(root,"package.json")
        found_files.append(temp_path)
        
def extract_dependencies_from_package_json(path):
    dependecies = {}
    with open(path,'r') as file:
        data = json.load(file)
        if "dependencies" in data:
            dependecies.update(data["dependencies"])
        if "devDependencies" in data:
            dependecies.update(data["devDependencies"])

    return dependecies
def extract_dependencies_from_requirement_txt(path):
    dependecies = []
    with open(path,'r') as file:
        for line in file:
            dependency = file.strip()
            if dependency:
                dependecies.append(dependency)

    return dependecies

for file_path in found_files:
    if file_path.endswith("package.json"):
        print(f"Dependencies in {file_path}:")
        dependencies =extract_dependencies_from_package_json(file_path)
        for dep,version in dependencies.items():
            print(dep,':',version)
    elif file_path.endswith("requirements.txt"):
        print(f"Dependencies in {file_path}:")
        dependencies =extract_dependencies_from_requirement_txt(file_path)
        for dep in dependencies:
            print(dep)
            
    
