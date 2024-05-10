from chatbot import add_contact, change_contact, show_phone, show_all

command_hello = {"hello"}
command_change = {"change"}
command_phone = {"phone"}
command_add = {"add"}
command_all = {"all"}
command_exit = {"close", "exit"}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
             print(change_contact(args, contacts))
        elif command == "phone":
             print(show_phone(args, contacts))
        elif command == "all":
             print(show_all(contacts))


        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
