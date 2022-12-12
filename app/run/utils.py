import os 

def text_exists(file_path,text):
    lines=[]
    with open(file_path,"r") as file:
        lines=file.readlines()
    
    if text+'\n' in lines:
        return True
    else:
        return False