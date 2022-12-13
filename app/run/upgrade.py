import subprocess
import os
from .utils import generate_sub_dependencies
import cmd_colors

def upgrade(command,requirements_path):
    len_command=len(command)-1
    upgraded_package=""
    if command[len_command]== "--upgrade" or command[len_command]=='-U':
        upgraded_package=command[len_command-1]
    else:
        upgraded_package=command[len_command]

    first_part=""
    try:
        rip_index=upgraded_package.index('=')
        first_part=upgraded_package[:rip_index]
    except ValueError:
        first_part=upgraded_package

    subprocess.run(command)
    upgrade_info=subprocess.run([command[0],"-m","pip","show",first_part],universal_newlines = True,stdout = subprocess.PIPE)

    upgrade_info=upgrade_info.stdout.splitlines()
    needed_line=""
    for line in upgrade_info:
        if 'Version:' in line or 'version:' in line:
            needed_line=line
            needed_line=needed_line.replace('Version:','')
            needed_line=needed_line.replace('version:','')
            needed_line=needed_line.strip()
            
        else:
            pass
    newly_upgraded_package=first_part+"=="+needed_line
    newly_upgraded_package=newly_upgraded_package.strip()

    requirement_txt=[]
    with open(requirements_path,"r") as file:
        requirement_txt=file.readlines()

    del_line=""
    
    for line in requirement_txt:
        get_line=line
        try:
            index=get_line.index('=')
            get_line=get_line[:index]
        except ValueError:
            cmd_colors.print_message("Error","Unexpected Error,please ensure every package in requirements.txt has a specific version")
            return
        if first_part==get_line:
            del_line=line
            break

    try:
        index=requirement_txt.index(del_line)
        requirement_txt[index]=newly_upgraded_package+'\n'
    except ValueError:
        cmd_colors.print_message("Error","Can not find previous version in requirements.txt")
    
    

    with open(requirements_path,"w") as file:
        for line in requirement_txt:
            file.write(line)

    generate_sub_dependencies(command[0],first_part)
    
    






