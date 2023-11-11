# -*- coding: UTF-8 -*-

# Import
import os


# Clean terminal
def clean_terminal():
    # Conditional to clean terminal depending OS
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
