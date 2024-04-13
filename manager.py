
""" This is the core script file which runs administrative tasks."""


import sys
import os

os.system("color")


def main():
    try:
        from src.lib.manager import manager_main
    except ImportError as e:
        print("Couldn't import manager module from src/lib/manager/manager_main.py")
        print(e)

    manager_main.getArguments(sys.argv)


if __name__ == "__main__":
    main()