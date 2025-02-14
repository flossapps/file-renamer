#!/usr/bin/env xonsh

"""
File Renamer
https://github.com/flossapps/file-renamer

A desktop app for Linux and Windows for batch renaming files.
It's Free, Libre, Open Source Software (FLOSS).

Copyright (C) 2024 Carlos
GNU General Public License
https://www.gnu.org/licenses/gpl-3.0.html
"""

import sys
import os
import re
from pathlib import Path

# Colors
ESC="\u001B"       # Unicode
BLD = ESC + "[1m"  # Bold or brighter
DEF = ESC + "[0m"  # Default color and effects

def menu():
    print(BLD + 'FILE RENAMER' + DEF)
    print("1) Python Module")
    print("2) Python Wheel")
    print("3) Linux Portable")
    print("q) Quit")
    option = input("Enter Option: ")
    match option:
        case "1":
            py_module()
        case "2":
            py_wheel()
        case "q":
            print('Quit')
            exit()
        case _:
            print("Invalid option")
            print()
            menu()

def py_module():
    print()
    print(BLD + "Python Module" + DEF)
    print("1) Install")
    print("2) Run")
    print("3) Remove")
    print("m) Main Menu")
    print("q) Quit")
    option = input("Enter Option: ")
    match option:
        case "1":
            py_module_install()
        case "2":
            py_module_run()
        case "3":
            py_module_remove()
        case "m":
            print()
            menu()
        case "q":
            print('Quit')
            sys.exit()
        case _:
            print("Invalid option")
            print()
            py_module()

def py_module_install():
    print("Install")
    python3 -m pip install -e .
    py_module()

def py_module_run():
    print("Run")
    python3 -m file_renamer
    py_module()

def py_module_remove():
    print("Remove")
    pip uninstall -y io.github.flossapps.file-renamer
    py_module()

def py_wheel():
    print()
    print(BLD + "Python Wheel" + DEF)
    print("1) Build")
    print("2) Install")
    print("3) Run")
    print("4) Remove")
    print("m) Main Menu")
    print("q) Quit")
    option = input("Enter option: ")
    match option:
        case "1":
            py_wheel_build()
        case "2":
            py_wheel_install()
        case "3":
            py_wheel_run()
        case "4":
            py_wheel_remove()
        case "m":
            print()
            menu()
        case "q":
            print('Quit')
            sys.exit()
        case _:
            print("Invalid option")
            print()
            py_wheel()

def py_wheel_build():
    print("Build")
    python3 -m build
    py_wheel()

def py_wheel_install():
    print("Install")
    pip install /data/fr/file-renamer/dist/io.github.flossapps.file_renamer-*.whl
    py_wheel()

def py_wheel_run():
    file-renamer
    py_wheel()

def py_wheel_remove():
    pip uninstall -y io.github.flossapps.file-renamer
    py_wheel()

clear
menu()
