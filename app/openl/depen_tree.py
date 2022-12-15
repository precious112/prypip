import os
import json
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def open_dependency_tree():

    '''
    open_dependency_tree function is responsible 
    for printing out every package with it's
    respective packages it depends on(dependencies)
    into an organized tree structure,it helps prevent
    clutering the requirements.txt with sub dependencies not pip
    installed directly.
    '''
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

