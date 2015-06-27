put KivyJSClient.java inside src/org/android/renpy/
build.py modified for allowing python files ( brython ) in the directory game/*.py

you will need INTERNET permissions:
python build.py --package com.br0bby.bgs4a --name bgs4a_poc --version 1.0 --permission INTERNET --dir folder_to_kivy_app debug
