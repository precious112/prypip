import colorama
from colorama import Fore

colorama.init(autoreset=True)

'''
print_message function is responsible for
printing console messages.
'''

def print_message(type,message):
    if type=="Error":
        print(f'{Fore.RED}Error:{message}')
    if type=="Warning":
        print(f'{Fore.YELLOW}Warning:{message}')
    if type=="Norm":
        print(f'{message}')
