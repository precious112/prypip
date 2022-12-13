import os
import json
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def open_dependency_tree():
    current_path=os.getcwd()
    dependency_tree=os.path.join(current_path,"dependency_tree.json")
    if os.path.exists(dependency_tree):
        tree_dict={}
        with open(dependency_tree,"r") as file:
            tree_dict=file.read()
        tree_dict=json.loads(tree_dict)
        for key in tree_dict:
            print("|"+"\n")
            print(" ---"+" "+key+"\n")
            print(Fore.RED+"    |"+"\n")
            print(Fore.BLUE+"     ---"+" "+tree_dict[key]+"\n")

