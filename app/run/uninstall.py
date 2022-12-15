import subprocess
import os
from .utils import text_exists,remove_sub_dependencies
from ..cmd_colors import print_message

def uninstall(commands,python_path,packages_path):
    requirements_path=os.path.join(os.getcwd(),"requirements.txt")
    final_command=[python_path]+commands
    final_command.insert(1,'-m')

    len_final_command=len(final_command)-1
    uncut_uninstalled_package=final_command[len_final_command]
    check=text_exists(requirements_path,uncut_uninstalled_package)

    if check==False:
        print_message("Error","package does not exists in requirements.txt,please make sure your site-packages match your requirements.txt")
        return

    subprocess.run(final_command)
    
    uninstalled_package=uncut_uninstalled_package
    
    try:
        version_index=uninstalled_package.index('=')
        uninstalled_package=uninstalled_package[:version_index]
    except ValueError:
        pass

    packages=os.listdir(packages_path)
    if uninstalled_package in packages:
        print("error")

    else:
        reqs=[]
        with open(requirements_path,"r") as requirements:
            reqs=requirements.readlines()
        
        
        try:
            package_index=reqs.index(uncut_uninstalled_package+'\n')
            del reqs[package_index]
        except ValueError:
            print_message("Error","can't find package in requirements.txt to remove it.")
            return
        
        with open(requirements_path,"w") as requirements:
            for req in reqs:
                requirements.write(req)

    remove_sub_dependencies(final_command[0],uninstalled_package)
