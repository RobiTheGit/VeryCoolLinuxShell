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
    print(f"Welcome to this shell. To access the menu at the top, type 'exit'.\nThis is in version {version}")
    
    while True:
        printStatusBar("Time: " + datetime.datetime.now().strftime("%I:%M") + "    Date: " + datetime.datetime.now().strftime("%Y/%m/%d"))
        
        if command != "exit":
            # Get input with some ansi escape codes. The code is very unreadable - but is it really a problem since it doesn't often need to be changed?
            command = input("\033[31;4;1m" + os.popen("whoami").read().split()[0] + "\033[0m@\033[33m" + os.popen("uname -n").read().split()[0] + "\033[0m~\033[36m" + os.popen("pwd").read().split("\n")[0] + "/\033[0m~$ ")
# Basically, What it does is, (also, the ansi codes are for colors)
# 1: Runs the command "whoami" which lets the shell tell who is using the main machinne
# 2: We then run "uname -n" which tells the shell what the name of the system is
# 3: We then run PWD which gives us our current working directory
# 4: we add the "~$ " and then after that is where the user types their command in

# The ansi codes are:
# \033[0m reset colors
# \033[31;4;1m red
# \033[33m yellow/orange
# \033[36m cyan

            try:
                if command.split()[0] == "ls":
                    command += " --color=yes"

                os.system(command) # Run the command with the os module, using sh
                # For changing directories
                try:
                    if command.split()[0] == "cd":
                        os.chdir(command.split()[1])
                except:
                    pass

            except:
                pass

        else:
            openNewProgram()

# Display things like information about the version, etc - maybe press any key to continue
def bootupScreen():
    os.system("clear")
    print(f"\033[0mVery Cool Linux Shell\nVersion {version}\n\nInformation:\n\n{info.read()}\n\nPress Any Key To Continue")
    wait_key()
    

bootupScreen()
terminalShell()
