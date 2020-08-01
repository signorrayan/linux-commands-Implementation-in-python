#This file depends on 'ls.py' file in the branch.

import os, sys
from colorama import Fore, Style



BOLD = '\033[1m'

def process_l(path):
    """
    this function will list the files (except hidden files.)
    """
    currentDirectory = os.getcwd()
    if path.startswith('./'): #convert to $FULL_PATH
        path = os.path.join(currentDirectory, path.lstrip('./'))

    if os.path.isdir(path):
        for file_dir in reversed(os.listdir(path)): #read every file in the directory list And apply the following commands to each of them
            mask = oct(os.stat(file_dir).st_mode)[-3:] #dir/file permessions.
            rwx = symbolic_notation(mask) #this function will convert the mask number to 'rwx' format
            if file_dir.startswith('.'):
                continue
            else:
                check_dir_file(file_dir, rwx)
    else:
        print("There is not a directory")


def process_la(path):
    """
    this function will list all files (including hidden files.)
    """
    currentDirectory = os.getcwd()
    if path.startswith('./'):
        path = os.path.join(currentDirectory, path.lstrip('./'))
    if os.path.isdir(path):
        for file_dir in reversed(os.listdir(path)):
            mask = oct(os.stat(file_dir).st_mode)[-3:]
            rwx = symbolic_notation(mask)
            check_dir_file(file_dir, rwx)

    else:
        print("There is not a directory")


def check_dir_file(file_dir, rwx):
    if os.path.isdir(file_dir):
        print(f"d{rwx:10} {BOLD}{Fore.GREEN}{file_dir}{Style.RESET_ALL}")
    else:
        print(f"-{rwx:10} {file_dir}")


def symbolic_notation(mask):
    """
    to convert the Mask numbers to symbolic notation 'rwx'.
    """
    r = 4
    w = 2
    x = 1
    end_rwx = ''
    for p in str(mask):
        rwx = ''
        p = int(p)
        if r <= p:
            p -= r
            rwx += 'r'

            if w <= p:
                p -= w
                rwx += 'w'
                if x <= p:
                    p -= x
                    rwx += 'x'
                else:
                    rwx += '-'

            elif x <= p:
                p -= x
                rwx += '-x'

            else:
                rwx += '--'

        elif w < p:
            p -= w
            rwx += '-w'
            if x <= p:
                p -= x
                rwx += 'x'
            else:
                rwx += '-'

        elif x <= p:
            p -= x
            rwx += '--x'

        end_rwx += rwx

    return end_rwx