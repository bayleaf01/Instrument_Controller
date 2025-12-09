import regex

commands = ["help", "showinst", "selectinst", "createcom",
             "cominst", "auto", "stopauto", "savelog", "reset", "saveset", "end"]

def print_help(commands):
    i = 0
    for i in range(len(commands)):
        print(commands[i]) #The i will come in handy when I add descriptions.

def user_command():
    user_in = input()
    command = regex.match(r"(\w+)\s\-\-(\w+)\s(\w+)", user_in)

    print(command)
    
    if len(command) == 0:
        print(f"Input {user_in} not recognised.")
    if command[0] not in commands:
        print(f"Command {command[0]} not recognised.")

    if command == "end":
        return False
    elif command == "help":
        print_help()
    return True

def run():
    running = True
    while running:
        running = user_command()

if __name__ == "__main__":
    run()