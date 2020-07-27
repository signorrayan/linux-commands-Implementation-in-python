import process
import os, sys

def main():
    script = sys.argv[0]
    path = sys.argv[2]
    action = sys.argv[1]
    assert action in ['-l', '-a', '-la'],\
            'Action is not one of -l, -a: ' + action
    action_righs(action, path)


def action_righs(action, path):
    if action == '-l':
        process.process_l(path)

    elif action == '-a' or '-la':
        process.process_la(path)


if __name__ == '__main__':
    main()