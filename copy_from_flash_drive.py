import os
import subprocess
import shutil
from datetime import datetime
the_suffix = (".jpg", ".png", ".txt")
dest = '/home/pytm/Desktop/Flash/'

paths = subprocess.Popen("lsblk", stdout=subprocess.PIPE, shell=True)
for output in paths.communicate()[0].split():
    if '/media/' in str(output):
        path = str(output, 'utf-8')
        dest_path = os.path.join(dest, os.path.basename(path))
        os.mkdir(dest_path)

def tree_find(path):
    files = os.listdir(path)
    try:
        for f in files:
            f = f"{path}/{f}"
            if os.path.isdir(f):
                new_path = f"{f}"
                tree_find(new_path)

            elif os.path.isfile(f):
                if os.path.basename(f).endswith(the_suffix):
                    shutil.copy2(f, dest_path)
    except Exception as e:
        print(e)
tree_find(path)
