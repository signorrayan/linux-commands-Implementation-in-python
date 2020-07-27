from symbolic import symbolic_notation
import os, sys

currentDirectory = os.getcwd()

def main():
    script = sys.argv[0]
    #switches = sys.argv[2]
    path = sys.argv[1]
    process(path)

def process(path):
    if path.startswith('./'):
        path = f"{currentDirectory}/{path.lstrip('./')}"
    for file_dir in reversed(os.listdir(os.getcwd())):
        mask = oct(os.stat(file_dir).st_mode)[-3:]
        rwx = symbolic_notation(mask)
        if os.path.isdir(file_dir):
            print(f"d{rwx:10} {file_dir}", end='\n')
        else:
            print(f"-{rwx:10} {file_dir}", end='\n')


if __name__ == '__main__':
    main()