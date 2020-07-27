from shutil import copy2, copytree
import sys
import os

currentDirectory = os.getcwd()

def main():
    script = sys.argv[0]
    source = sys.argv[1]
    destination = sys.argv[2]
    process(source, destination)


def destination_check(source, destination, action):
    if destination.startswith('./'):  #exp: cp ./filename ./other_destination_directory/
        destination = f"{currentDirectory}/{destination.lstrip('./')}"
        if os.path.isdir(os.path.dirname(destination)):  # if ./other_destination_directory Exists
            try:
                action

            except NotADirectoryError:
                return "There isn't a directory"

    else:
        if os.path.isdir(os.path.dirname(destination)):
            action


def process(source, destination):
    if source.startswith('./'):  # cp ./filename /destination_path
        source = f"{currentDirectory}/{source.lstrip('./')}"
        if os.path.isfile(source):
            try:
                destination_check(source, destination, copy2(source, destination))

            except NotADirectoryError as nd:
                return f'No Such file or directory! {nd}'

        elif os.path.isdir(source):
            try:
                destination_check(source, destination, copytree(source, destination))

            except NotADirectoryError as nd:
                return f'No Such file or directory! {nd}'

    elif destination.startswith('./'):
        try:
            destination = f"{currentDirectory}/{destination.lstrip('./')}"
            if os.path.isfile(source):
                destination_check(source, destination, copy2(source, destination))

            elif os.path.isdir(source):
                destination_check(source, destination, copytree(source, destination))

        except NotADirectoryError as nd:
            return f'No Such file or directory! {nd}'

        except PermissionError:
            return 0


if __name__ == '__main__':
    main()


# # Copying files using subprocess module
# # subprocess.call signature
# # subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
# # # example (WARNING: setting `shell=True` might be a security-risk)
# # # In Linux/Unix
# # status = subprocess.call('cp source.txt destination.txt', shell=True)