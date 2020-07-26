from shutil import copy2, copytree
import sys
import os

currentDirectory = os.getcwd()

def main():
    script = sys.argv[0]
    source = sys.argv[1]
    destination = sys.argv[2]
    process(source, destination)


def destination_check(src, destination, action):
    if destination.startswith('./'):  #exp: cp ./filename ./other_destination_directory/
        destination = f"{currentDirectory}/{destination.lstrip('./')}"
        if os.path.isdir(os.path.dirname(destination)):  # if ./other_destination_directory Exists
            action

        else:
            print("There isn't a directory")

    else:
        if os.path.isdir(os.path.dirname(destination)):
            action


def process(source, destination):
    if source.startswith('./'):  # cp ./filename /destination_path
        source = f"{currentDirectory}/{source.lstrip('./')}"
        if os.path.isfile(source):
            dst_check(source, destination, copy2(source, destination))

        elif os.path.isdir(source):
            dst_check(source, destination, copytree(source, destination))

        else:
            print('No Such file or directory!')

    elif destination.startswith('./'):
        destination = f"{currentDirectory}/{destination.lstrip('./')}"
        if os.path.isfile(source):
            dst_check(source, destination, copy2(source, destination))

        elif os.path.isdir(source):
            dst_check(source, destination, copytree(source, destination))

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