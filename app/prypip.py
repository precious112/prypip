#!/usr/bin/env python3

import sys
import os
from .run.main import run
from .openl.main import openl
from .cmd_colors import print_message

'''
the main entry point of the prypip project,here's where
the prypip command line tool keyword emanates.
'''


def main():
    #get the list of the specified command using sys.argv
    command_list=sys.argv
    
    

    if len(command_list)<2:
        print_message("Error","No commands and arguments specified.")
        return

    #remove the first item in command_list since it's the generic prypip command
    del command_list[0] 

    #using prypip will require having venv_py_path.txt at the root of the project's directory
    #with the path to the python interpreter present within the current activated virtual environment 
    #of the project specified in the venv_py_path.txt
    
    venv_py_path="venv_py_path.txt"
    venv_py_path=os.path.join(os.getcwd(),venv_py_path)
   
    if os.path.isfile(venv_py_path):
        python_path=""
        packages_path=""
        with open("venv_py_path.txt","r") as py_path:
            #get path to venv python interpreter in the file
            python_path=py_path.readline().strip('\n')
            packages_path=py_path.readline()
            

        if len(python_path)<=0 and len(packages_path)<=0:
            print_message("Error","you haven't specified the current activated virtual environment's python interpreter in the venv_py_path")
            
        if command_list[0]=="run":
            passed_commands=command_list[1:] 
            run(passed_commands,python_path,packages_path)

        if command_list[0]=="open":
            openl(command_list[1])
    else:
        print_message("Error","prypip can't find your venv_py_path.txt,add the file to use prypip.")

    

#if __name__ == "__main__":
    #main()