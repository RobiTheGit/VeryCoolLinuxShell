#!/usr/bin/python3
import datetime
import time
import sys
import os
import wordProcessor
from console.utils import wait_key
info = open("README.md", "r")
version = "0.2.0"

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines

# For printing the status bar menu at the top of the screen with ANSI escape character codes:
def printStatusBar(statusBarMessage):
    statusBarMessageANSI = "\033[44m" + statusBarMessage
    print(f"\033[0;0H{statusBarMessageANSI}", end="")

    # Whitespace at the end of the statusBarMessage line:
    for _ in range(len(statusBarMessage), os.get_terminal_size().columns):
        print(" ", end="")

    print("\033[0m", end="") # Reset the colors

    print(f"\033[{os.get_terminal_size().lines};0H", end="") # Put the cursor at the bottom of the page

def openNewProgram():
    inputMessage = "1. Exit; 2. Word Processor; 3. Restart: "
    printStatusBar(inputMessage)

    option = input("\033[0;{0}H".format(len(inputMessage)+1)) # Put the cursor in the correct place and get input

    if option == "1":
        os.system("clear")
        sys.exit()

    elif option == "2":
        wordProcessor.main()
        terminalShell() # After the program is finished, restart the terminal shell

    elif option == "3":
        terminalShell()

def terminalShell():
    command = ""

    # Setup:
    os.system("clear")
    print(f"\033[{os.get_terminal_size().lines};0H", end="")
    print(f"Welcome to this shell. To access the menu, type 'exit'.\nThis is in version {version}")
    printStatusBar("Time: " + datetime.datetime.now().strftime("%I:%M") + "    Date: " + datetime.datetime.now().strftime("%Y/%m/%d"))
    os.system("bash")
    openNewProgram()

# Display things like information about the version, etc - maybe press any key to continue
def bootupScreen():
    os.system("clear")
    print(f"\033[0mVery Cool Linux Shell\nVersion {version}\n\nInformation:\n\n{info.read()}\n\nPress Any Key To Continue")
    wait_key()
    

bootupScreen()
terminalShell()
