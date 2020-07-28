#this script use the "process.py" file in the branch to process the listing items.
# ls {-l, -a, -la} path

import process
import os, sys

def main():
    script = sys.argv[0]
    action = sys.argv[1] #switches that we use after the scripts
    path = sys.argv[2]

    assert action in ['-l', '-a', '-la'],\
            'Action %s is not one of -l, -a: ' % action #if the switches was not one of these, the error will raised.
    action_righs(action, path)

def action_righs(action, path):
    if action == '-l':
        process.process_l(path) #this function will call when we want normal files (not hidden)

    elif action == '-a' or '-la':
        process.process_la(path) #this function will call when we want all files(including hidden files).

if __name__ == '__main__':
    main()