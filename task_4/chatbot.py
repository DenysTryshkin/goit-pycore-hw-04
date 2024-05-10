def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Name of phone number is not correct! Please write name and phone number!"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    


def change_contact (args, contacts):
    try:
        name, phone = args
        if name not in contacts:
            return "Contact does not exist"
        contacts[name] = phone
        return "Contact updated."
    except ValueError:
        return "Name of phone number is not correct! Please write name and phone number!"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    


def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    


def show_all(contacts):
    try:
        if contacts:
            return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        else:
            return "No contacts saved."
    except Exception as e:
        return f"An error occurred: {str(e)}"