import os, shutil, sys


currentDirectory = os.getcwd()

def main():
    script = sys.argv[0]
    switch_path = sys.argv[1:]
    if switch_path:
        if switch_path[0].startswith('-'): #if we have a switch -r, it means we want to delete a directory reqursively
            switch = switch_path[0]
            assert switch in ['-r'], 'Switch can be -r to delete a directory reqursively!'
            path = switch_path[1]
            remove_directory(path) #the remove_directory

        else: #if we don't pass any switch, it means we want to delete file/files.
            path = switch_path[0:]
            for file in path:
                #if we have more that one file that psased after the script, this loop will remove all passed arguments
                remove_file(file)

def remove_file(path):
    if path.startswith('./'):
        path = f"{currentDirectory}/%s" %path.lstrip('./')
    if os.path.isdir(path):
        print("To delete a directory, pass -r switch after command")
        exit()
    os.remove(path)

def remove_directory(path):
    if path.startswith('./'):
        path = f"{currentDirectory}/%s" %path.lstrip('./')
    if os.path.isfile(path):
        print("To delete a file, don't use -r switch")
        exit()
    shutil.rmtree(path)



if __name__ == '__main__':
    main()