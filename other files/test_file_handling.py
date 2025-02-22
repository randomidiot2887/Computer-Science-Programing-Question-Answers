import os
def print_file(filename): #To print filecontents on startup
    file = open(filename, "r")
    text = file.read()
    file.close()
    print(f"-----------------------------------------------------------\nContents of file {filename}\n-----------------------------------------------------------\n{text}\n-----------------------------------------------------------")
def append_file(filename): #Appending to existing file contents
    file = open(filename, "a")
    text_to_store = ""
    try:
        print("Input the text you wanna put in the file. press CTRL+C to exit")
        while True:
            text_to_store = text_to_store + f"{input(": - ")}\n"
    except:#If error occurs, save and exit (like CTRL+C)
        file.write(text_to_store)
        file.close()
def clear_file(filename):#Clearing the file
    file = open(filename, "w")
    file.write("")
    file.close
def write_file(filename):#Writing file, deleting existing contents
    file = open(filename, "w")
    text_to_store = ""
    try:
        print("Input the text you wanna put in the file. press CTRL+C to exit")
        while True:
            text_to_store = text_to_store + f"{input(": - ")}\n"
    except:#If error occurs, save and exit (like CTRL+C)
        file.write(text_to_store)
        file.close()

    
while True:   #getting filename
    print("Welcome to simple notepad V1 CLI")
    filename = input("Input the name of the file you want to open\n: - ")
    try:#If files there
        print_file(filename)
        break
    except:#If npot, ask use to create it
        print("file doesnt exist\n")
        option = input("Do you want to create the file?\n(Y/N): - ")
        match option.upper():
            case "Y":
                clear_file(filename); break
            case "N":
                print("ok.")
while True:
    try:#If not CTRL+C
        read_or_write = (input(f"For file {filename}\n Do you want to (A)ppend file or (W)rite file or (C)lear file or (D)isplay File?\n(A/W/C/D)]\nDo CTRL + C to exit\n|: - "))
        match read_or_write.upper():
            case "A":
                append_file(filename)
            case "C":
                clear_file(filename)
            case "W":
                write_file(filename)
            case "D":
                print_file(filename)
    except:#If error occures, exit.
        print("exiting program")
        break