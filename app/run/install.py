import subprocess
import os
from .utils import text_exists,check_for_upgrade,generate_sub_dependencies
from .upgrade import upgrade
from ..cmd_colors import print_message





def install(commands,python_path,packages_path):
    #os.system("cls")
    requirements_path=os.path.join(os.getcwd(),"requirements.txt")
    print(requirements_path)
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
        print_message("Error","package exists in requirements.txt,please make sure your site-packages match your requirements.txt")
        return

    subprocess.run(final_command)

    installed_package=uncut_installed_package
    version=None
    #print(installed_package)
    try:
        version_index=installed_package.index('=')
        installed_package=installed_package[:version_index]
    except ValueError:
        version_info=subprocess.run([final_command[0],"-m","pip","show",installed_package],universal_newlines = True,stdout = subprocess.PIPE)
        version_info=version_info.stdout.splitlines()
        needed_line=""
        for line in version_info:
            if 'Version:' in line or 'version:' in line:
                needed_line=line
                needed_line=needed_line.replace('Version:','')
                needed_line=needed_line.replace('version:','')
                needed_line=needed_line.strip()
            else:
                pass
        
        version=needed_line

    packages=os.listdir(packages_path)
    if installed_package in packages:
        with open(requirements_path,"a") as requirements:
            
            if version==None:
                requirements.write(uncut_installed_package+'\n')
            else:
                exact_package=installed_package+"=="+version
                exact_package=exact_package.strip()
                requirements.write(exact_package+'\n')

    generate_sub_dependencies(final_command[0],installed_package)

