import os 

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
                print(f'you are trying to install {first_part_text} which is already in your list of depencies as {line}')
                print('please specify the version incase you are trying to upgrade or downgrade this current package')
                return False
            if last_part_line==last_part_text:
                print('package already exists in requirements.txt')
                return False
            else:
                return True
        else:
            pass
    return f'pass'