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
import glob
import subprocess

# Colors
ESC = "\u001B"     # Unicode
BLD = ESC + "[1m"  # Bold or brighter
DEF = ESC + "[0m"  # Default color and effects

# File Renamer Dict
fr = {
    'name': 'File Renamer',
    'id': 'io.github.flossapps.file-renamer',
    'cli': 'file-renamer'
}


def menu():
    print(BLD + fr['name'].upper() + DEF)
    print("1) Python Module")
    print("2) Python Wheel")
    if $platform == "Windows":
        print("3) Windows Portable")
    else:
        print("3) Linux Portable")
    print("q) Quit")
    option = input("Enter Option: ")
    match option:
        case "1":
            py_module()
        case "2":
            py_wheel()
        case "3":
            # linux_portable()
            portable()
        case "q":
            print('Quit')
            exit()
        case _:
            print("OPTION NOT AVAILABLE")
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
            print("OPTION NOT AVAILABLE")
            print()
            py_module()


def py_module_install():
    print("Install")
    output = subprocess.run(
        ["python3", "-m", "pip", "list", "--editable"], stdout=subprocess.PIPE
    )
    output_str = output.stdout.decode('UTF-8')
    result = re.search(fr['id'], output_str)
    if result is None:
        subprocess.run(["python3", "-m", "pip", "install", "-e", "."])
    else:
        print('ALREADY INSTALLED:', fr['id'])
    py_module()


def py_module_run():
    print("Run")
    output = subprocess.run(
        ["python3", "-m", "pip", "list"], stdout=subprocess.PIPE
    )
    output_str = output.stdout.decode('UTF-8')
    result = re.search(fr['id'], output_str)
    if result is None:
        print('NOT FOUND:', fr['id'])
    else:
        subprocess.run(["python3", "-m", "file_renamer"])
    py_module()


def py_module_remove():
    print("Remove")
    output = subprocess.run(
        ["python3", "-m", "pip", "list"], stdout=subprocess.PIPE
    )
    output_str = output.stdout.decode('UTF-8')
    result = re.search(fr['id'], output_str)
    if result is None:
        print('NOT FOUND:', fr['id'])
    else:
        subprocess.run(["pip", "uninstall", "-y", fr['id']])
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
            print("OPTION NOT AVAILABLE")
            print()
            py_wheel()


def py_wheel_build():
    print("Build")
    subprocess.run(["python3", "-m", "build"])
    py_wheel()


def py_wheel_install():
    print("Install")
    if $platform == "Windows":
        whl = $project_path + '\\dist\\*.whl'
    else:
        whl = $project_path + '/dist/*.whl'
    output = subprocess.run(
        ["python3", "-m", "pip", "list"], stdout=subprocess.PIPE
    )
    output_str = output.stdout.decode('UTF-8')
    result = re.search(fr['id'], output_str)
    if result is None:
        for f in glob.glob(whl):
            subprocess.run(["pip", "install", f])
    else:
        print('ALREADY INSTALLED:', fr['id'])
    py_wheel()


def py_wheel_run():
    print("Run")
    output = subprocess.run(
        ["python3", "-m", "pip", "list"], stdout=subprocess.PIPE
    )
    output_str = output.stdout.decode('UTF-8')
    result = re.search(fr['id'], output_str)
    if result is None:
        print('NOT FOUND:', fr['id'])
    else:
        subprocess.run(fr['cli'])
    py_wheel()


def py_wheel_remove():
    print("Remove")
    output = subprocess.run(
        ["python3", "-m", "pip", "list"], stdout=subprocess.PIPE
    )
    output_str = output.stdout.decode('UTF-8')
    result = re.search(fr['id'], output_str)
    if result is None:
        print('NOT FOUND:', fr['id'])
    else:
        subprocess.run(["pip", "uninstall", "-y", fr['id']])
    py_wheel()


def portable():
    print()
    if $platform == "Windows":
        print(BLD + "Windows Portable" + DEF)
    else:
        print(BLD + "Linux Portable" + DEF)
    print("1) Build")
    print("2) Run")
    print("3) Remove")
    print("m) Main Menu")
    print("q) Quit")
    option = input("Enter option: ")
    match option:
        case "1":
            portable_build()
        case "2":
            portable_run()
        case "3":
            portable_remove()
        case "m":
            print()
            menu()
        case "q":
            print('Quit')
            sys.exit()
        case _:
            print("OPTION NOT AVAILABLE")
            print()
            portable()


def portable_build():
    print("Build")
    if $platform == "Windows":
        spec = $project_path + "\\spec\\app-win.spec"
    else:
        spec = $project_path + "/spec/app-linux.spec"  
    subprocess.run(["pyside6-deploy", "-v", "-c", spec])
    portable()


def portable_run():
    print("Run")
    if $platform == "Windows":
        portable_file = $project_path + '\\deploy\\file-renamer.exe'
    else:
        portable_file = $project_path + '/deploy/file-renamer'
    try:
        if os.path.exists(portable_file) is False:
            raise FileNotFoundError()
    except FileNotFoundError:
        print('FILE NOT FOUND:', portable_file)
        portable()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        portable()
    else:
        subprocess.call(portable_file, shell=True)
        portable()


def portable_remove():
    print("Remove")
    if $platform == "Windows":
        portable_file = $project_path + '\\dist\\file-renamer.exe'
    else:
        portable_file = $project_path + '/dist/file-renamer'
    try:
        if os.path.exists(portable_file) is False:
            raise FileNotFoundError()
    except FileNotFoundError:
        print('FILE NOT FOUND:', portable_file)
        portable()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        portable()
    else:
        subprocess.run(["rm", "--verbose", portable_file])
        portable()


clear
menu()
