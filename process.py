import os, sys
from colorama import Fore, Back, Style
# from symbolic import symbolic_notation

currentDirectory = os.getcwd()
BOLD = '\033[1m'

def process_l(path):
    if path.startswith('./'):
        path = f"{currentDirectory}/{path.lstrip('./')}"
    for file_dir in reversed(os.listdir(os.getcwd())):
        mask = oct(os.stat(file_dir).st_mode)[-3:]
        rwx = symbolic_notation(mask)

        if file_dir.startswith('.'):
            continue
        elif os.path.isdir(file_dir):
            print(f"d{rwx:10} {BOLD}{Fore.GREEN}{file_dir}{Style.RESET_ALL}")
        else:
            print(f"-{rwx:10} {file_dir}")


def process_la(path):
    if path.startswith('./'):
        path = f"{currentDirectory}/{path.lstrip('./')}"
    for file_dir in reversed(os.listdir(os.getcwd())):
        mask = oct(os.stat(file_dir).st_mode)[-3:]
        rwx = symbolic_notation(mask)

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