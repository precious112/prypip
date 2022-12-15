from .install import *
from .uninstall import *

'''
this  module is in charge of running external commands outside of prypip
an example is pip and uninstall 
'''

def run(command,python_path,packages_path):
    if command[0]=="pip":
        if command[1]=="install":
            install(command,python_path,packages_path)
            
        if command[1]=="uninstall":
            uninstall(command,python_path,packages_path)