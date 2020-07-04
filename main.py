import datetime
import sys
import os

version = "0.2.0"

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines

# For printing the status bar menu at the top of the screen with ANSI escape character codes:
def printStatusBar(statusBarMessage):
    statusBarMessageANSI = "\033[44m" + statusBarMessage
    print(f"\033[0;0H{statusBarMessageANSI}", end="")

    # Whitespace at the enf of the statusBarMessage line:
    for i in range(len(statusBarMessage), os.get_terminal_size().columns):
        print(" ", end="")

    print("\033[0m", end="") # Reset the colors

    print(f"\033[{os.get_terminal_size().lines};0H", end="") # Put the cursor at the bottom of the page

def openNewProgram():
    inputMessage = "1. Exit; 2. Terminal: "
    printStatusBar(inputMessage)

    option = input("\033[0;{0}H".format(len(inputMessage)+1)) # Put the cursor in the correct place and get input

    if option == "1":
        os.system("clear")
        sys.exit()

    elif option == "2":
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
            command = input("\033[31;4m" + os.popen("whoami").read().split()[0] + "\033[0m@\033[33m" + os.popen("uname -n").read().split()[0] + "\033[0m~\033[36m" + os.popen("pwd").read().split("\n")[0] + "/\033[0m~$ ")

            os.system(command) # Run the command with the os module

            # For changing directories
            try:
                if command.split()[0] == "cd":
                    os.chdir(command.split()[1])
            except:
                pass

        else:
            openNewProgram()

# Display things like information about the version, etc - maybe press any key to continue
def bootupScreen():
    pass

bootupScreen()
terminalShell()
