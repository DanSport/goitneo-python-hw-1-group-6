#import moskali

MENU = """
    * Available commands:
        #1 or hello
        #2 or add
        #3 or change
        #4 or get
        #5 or all
        #6 or close or exit or bye
"""
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Please provide name and phone number separated by space."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def get_contact(search_term, contacts):
    for name, phone in contacts.items():
        if search_term.lower() in (name.lower(), phone.lower()):
            return (f"Contact: {name} - Phone Number: {phone}")        
        else:
            return ("Contact not found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print(MENU)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye" , "6"]:
            print("Good bye!")
            break
        elif command in ["hello", "1"]:
            print("How can I help you?")
            print(MENU)
        elif command in ["add", "2"] :
            user_input = input("Enter a name and phone number separated by space: \nexample: John 0504681533\nEnter here>>>>")
            print(add_contact(user_input.split(), contacts))
        elif command in ["change", "3"]:
            user_input = input("Enter the name of the contact to change and phone number separated by space: \nexample: John 0504681533\nEnter here>>>>")
            print(add_contact(user_input.split(), contacts))
        elif command in ["get", "4"]:
            search_term = input("Enter the name or phone number of the contact to get: ")
            print(get_contact(search_term, contacts))
        elif command in ["all", "5"]:
            for name, phone in contacts.items():
                print(f"{name:<15} {phone:<100}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()