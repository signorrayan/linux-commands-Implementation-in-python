from shutil import copy2
from distutils.dir_util import copy_tree
import sys
import os

currentDirectory = os.getcwd()

def main():
    script = sys.argv[0]
    source = sys.argv[1]
    destination = sys.argv[2]
    process(source, destination)


def destination_check(source, destination, action):
    if destination.startswith('./'):  #if it wasn't $FULLPATH change it to Full path
        destination = os.path.join(currentDirectory, destination.lstrip('./'))
    action


def process(source, destination):
    if source.startswith('./'):  # change the source path to $FULLPATH
        source = os.path.join(currentDirectory, source.lstrip('./'))

    if os.path.isfile(source): #if it was a file, use the copy2 method
        destination_check(source, destination, copy2(source, destination))

    elif os.path.isdir(source): #if it was a directory, reqursively copy the files
        destination_check(source, destination, copy_tree(source, destination))

    else:
        print('No Such file or directory!')


if __name__ == '__main__':
    main()


# # Copying files using subprocess module
# # subprocess.call signature
# # subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
# # # example (WARNING: setting `shell=True` might be a security-risk)
# # # In Linux/Unix
# # status = subprocess.call('cp source.txt destination.txt', shell=True)