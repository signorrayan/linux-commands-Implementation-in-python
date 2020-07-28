#This file depends on 'ls.py' file in the branch.

import os, sys
from colorama import Fore, Back, Style


currentDirectory = os.getcwd()
BOLD = '\033[1m'

def process_l(action, path):
    if path.startswith('./'):
        path = f"{currentDirectory}/{path.lstrip('./')}"
        if os.path.isdir(path):
            for file_dir in reversed(os.listdir(path)):
                mask = oct(os.stat(file_dir).st_mode)[-3:]
                rwx = symbolic_notation(mask) #this function will convert the mask number to 'rwx' format

                if file_dir.startswith('.'):
                        continue
                else:
                   check_dir_file(file_dir, rwx)

        else:
            print("There is not a directory")



def process_la(path):
    if path.startswith('./'):
        path = f"{currentDirectory}/{path.lstrip('./')}"
        if os.path.isdir(path):
            for file_dir in reversed(os.listdir(os.getcwd())):
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
    to convert the Mask into symbolic notation
    :param mask:
    :return:
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