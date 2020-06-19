import os, datetime

version = "1.0.0"
command = ""

# Display stuff at the start
os.system("clear")
print(f"""
Welcome to pyTermShell!
This program is version {version}
""")

# Put terminal stuff in a function, in the same file as app launcher
while True:
    now = datetime.datetime.now()

    os.system(command)

    # Exiting the terminal shell
    if command == "exit" or command == " exit" or command == "exit ":
        break

    # Changing directories:
    try:
        os.chdir(command.split()[1])

    except:
        pass

    length = len(command.split("\n"))

    command = input("\033[34;1m" + now.strftime("%H:%M~") + "\033[31m" + os.popen("whoami").read().split()[0] + "~\033[0m\033[36m" + os.popen("pwd").read().split("\n")[0] + "/\033[0m~$ ")
