import os
import subprocess
from pathlib import Path
import json
import cmd_colors

def text_exists(file_path,text):
    lines=[]
    with open(file_path,"r") as file:
        lines=file.readlines()
    
    if text+'\n' in lines:
        return True
    else:
        return False

def check_for_upgrade(file_path,text):
    lines=[]
    with open(file_path,"r") as file:
        lines=file.readlines()
    
    for line in lines:
        first_part_line=""
        last_part_line=""
        first_part_text=""
        last_part_text=""
        try:
            rip_index=line.index('=')
            first_part_line=line[:rip_index]
            last_part_line=line[rip_index:]
            last_part_line=last_part_line.replace("==",'')
            last_part_line=last_part_line.strip()
            
        except ValueError:
            first_part_line=line

        try:
            rip_index=text.index('=')
            first_part_text=text[:rip_index]
            last_part_text=text[rip_index:]
            last_part_text=last_part_text.replace("==",'')
            last_part_text=last_part_text.strip()
            
        except ValueError:
            first_part_text=text

        if first_part_line==first_part_text:
            if last_part_text=="":
                cmd_colors.print_message("Warning",f'You are trying to install {first_part_text} which is already in your list of depencies as {line}')
                cmd_colors.print_message("Warning",f'please specify the version incase you are trying to upgrade or downgrade this current package')
                return False
            if last_part_line==last_part_text:
                
                cmd_colors.print_message("Norm","Package already exists in requirements.txt")
                return False
            else:
                return True
        else:
            pass
    return f'pass'

def generate_sub_dependencies(python_path,package):
    current_path=os.getcwd()
    dependency_tree=os.path.join(current_path,"dependency_tree.json")
    if os.path.exists(dependency_tree):
        pass
    else:
        f=open('dependency_tree.json','x')
        f.close()
    
    sub_dependencies_raw=subprocess.run([python_path,"-m","pip","show",package],universal_newlines = True,stdout = subprocess.PIPE)
    sub_dependencies_raw=sub_dependencies_raw.stdout.splitlines()
    
    sub_dependencies=""
    for line in sub_dependencies_raw:
        if "Requires" in line or "requires" in line:
            sub_dependencies=line
            sub_dependencies=sub_dependencies.replace("Requires:","")
            sub_dependencies=sub_dependencies.replace("requires:","")
            sub_dependencies=sub_dependencies.strip()
            break


    current_file=Path(dependency_tree)
    new_dict={
            package:sub_dependencies
        }
    new_dict=json.dumps(new_dict)

    if current_file.stat().st_size ==0:
        with open('dependency_tree.json',"a") as file:
            file.write(new_dict)
    else:
        tree_dict={}
        with open('dependency_tree.json',"r") as file:
            tree_dict=file.read()
        tree_dict=json.loads(tree_dict)
        tree_dict[package]=sub_dependencies
        tree_dict=json.dumps(tree_dict)
        with open('dependency_tree.json',"w") as file:
            file.write(tree_dict)

        
def remove_sub_dependencies(python_path,package):
    current_path=os.getcwd()
    dependency_tree=os.path.join(current_path,"dependency_tree.json")
    if not os.path.exists(dependency_tree):
        cmd_colors.print_message("Error","dependency tree file does not exist,you propably didn't install this package with prypip")
        return False

    tree_dict={}
    with open(dependency_tree,"r") as file:
        tree_dict=file.read()

    tree_dict=json.loads(tree_dict)
    try:
        del tree_dict[package]
    except KeyError:
        cmd_colors.print_message("Error","package not present in dependency tree")
        return
    
    tree_dict=json.dumps(tree_dict)
    with open(dependency_tree,"w") as file:
        file.write(tree_dict)
