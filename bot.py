
def parse_input(user_input):    

    """Приймаємо від користувача дані і сортуємо на команди і аргументи,
    приводимо команди в нижній регістр, щоб уникнути помилок команд написаних з великої букви 
    і повертаєм команди в нижнтому регістрі, та аргументи які надав користувач"""

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError :
            return "Not enough arguments."

    return inner


@input_error
def add_contact(args, contacts):

    """При команді add, і наступних аргумантах name phone,
    перевіряємо чи ім'я є в словнику, якщо немає, додаємо його в словник,
    якщо є виводим повідомлення, що таке ім'я вже записане"""

    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "This name is already saved"
    

@input_error
def change_contact(args, contacts):

    """При команді change, шукаємо імя в словнику, якщо воно є,
    змінєюмо телефон, якщо немає виводим текст контакт не знайдений"""
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phone(args, contacts):

    """Шукаєм контакт в списку, і виводимо дані,
    якщо немає виводим повідомлення"""

    name = args[0]
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print(f'Number {name} is not saved')


@input_error
def show_all(contacts):

    """Виводимо весь список контактів"""

    if len(contacts) == 0:
        return "Phone book is empty"
    else:
        contact_list = "\n".join([f'Name: {name}, Phone: {number}' for name, number in contacts.items()])
        return contact_list


def main():
    """Функція приймає команди і аргументи і передає їх на виконання іншим функціями"""
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



# def parse_input(user_input):    
#     """Приймаємо від користувача дані і сортуємо на команди і аргументи,
#     приводимо команди в нижній регістр, щоб уникнути помилок команд написаних з великої букви 
#     і повертаєм команди в нижнтому регістрі, та аргументи які надав користувач"""

#     cmd, *args = user_input.split()
#     cmd = cmd.strip().lower()
#     return cmd, *args


# def add_contact(args, contacts):
#     """При команді add, і наступних аргумантах name phone,
#     перевіряємо чи ім'я є в словнику, якщо немає, додаємо його в словник,
#     якщо є виводим повідомлення, що таке ім'я вже записане"""

#     name, phone = args
#     if not name in contacts:
#         contacts[name] = phone
#         return "Contact added."
#     else:
#         return "This name is already saved"
    

# def change_contact(args, contacts):
#     """При команді change, шукаємо імя в словнику, якщо воно є,
#     змінєюмо телефон, якщо немає виводим текст контакт не знайдений"""
    
#     name, phone = args
#     if name in contacts:
#         contacts[name] = phone
#         return "Contact updated."
#     else:
#         return "Contact not found."
        

# def show_phone(args, contacts):
#     """Шукаєм контакт в списку, і виводимо дані,
#     якщо немає виводим повідомлення"""
#     name = args[0]
#     if name in contacts:
#         return(f"{name}: {contacts[name]}")
#     else:
#         return(f'Number {name} is not saved')

# def show_all(contacts):
#     """Виводимо весь список контактів"""
#     if len(contacts) == 0:
#         return "Phone book is empty"
#     else:
#         contact_list = "\n".join([f'Name: {name}, Phone: {number}' for name, number in contacts.items()])
#         return contact_list

        


# def main():
#     """Функція приймає команди і аргументи і передає їх на виконання іншим функціями"""
#     contacts = {}
#     print("Welcome to the assistant bot!")
#     while True:
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)

#         if command in ["close", "exit"]:
#             print("Good bye!")
#             break
#         elif command == "hello":
#             print("How can I help you?")
#         elif command == "add":
#             print(add_contact(args, contacts))
#         elif command == "change":
#             print(change_contact(args, contacts))
#         elif command == "phone":
#             print(show_phone(args, contacts))
#         elif command == "all":
#             print(show_all(contacts))
#         else:
#             print("Invalid command.")

# if __name__ == "__main__":
#     main()
