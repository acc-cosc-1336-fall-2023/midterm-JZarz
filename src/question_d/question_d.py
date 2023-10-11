#write functions here, don't add input('') statements here!
def rev_str(string):
    new_str = ""
    index = len(string) -1

    while index >= 0:
        new_str += string[index]
        index -= 1
    return new_str

def menu():
    string = input("enter a string you'd like to print in reverse: \n")

    new_str = rev_str(string)

    print (new_str)

    cont()

def cont():
    result = input ("Would you like to reverse another string?\n Type 'Y' for yes \n Type 'N' for no:\n")

    while result.upper() != "N":
        if result.upper() == 'Y':
            menu()
            
        else:
            while result.upper() != 'Y' and result.upper() != 'N':
                result = input("Please choose 'Y' or 'N': ")
    print("program exited")
    exit()