import subprocess
import os
from .utils import text_exists,check_for_upgrade
from .upgrade import upgrade
import cmd_colors


def install(commands,python_path,packages_path):
    requirements_path=os.path.join(os.getcwd(),"requirements.txt")
    final_command=[python_path]+commands
    final_command.insert(1,'-m')
    len_final_command=len(final_command)-1

    if final_command[len_final_command]=="--upgrade" or final_command[len_final_command]== '-U':
        upgrade(final_command,requirements_path)
        return

    uncut_installed_package=final_command[len_final_command]
    check=text_exists(requirements_path,uncut_installed_package)
    upgrade_pack=check_for_upgrade(requirements_path,uncut_installed_package)
    
    if upgrade_pack==True:
        upgrade(final_command,requirements_path)
        return
    
    if upgrade_pack==False:
        return
    
    if upgrade_pack=='pass':
        pass



    if check==True:
        print('Error: package exists in requirements.txt,please make sure your site-packages match your requirements.txt')
        return

    subprocess.run(final_command)

    installed_package=uncut_installed_package
    print(installed_package)
    try:
        version_index=installed_package.index('=')
        installed_package=installed_package[:version_index]
    except ValueError:
        pass

    packages=os.listdir(packages_path)
    if installed_package in packages:
        with open(requirements_path,"a") as requirements:
            
            requirements.write(uncut_installed_package+'\n')

