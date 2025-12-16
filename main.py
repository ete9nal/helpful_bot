from datetime import datetime



'''
{"text": "my note", "creation_date": "04.07.2024"}


1) Створити словник нотаток та записати в нього інфу
2) Написати функцію, яка буде виводити нотатку
3) Написати функцію, яка буде виводити усі нотатки
4) Написати цикл, який буде отримувати інформацію від користувача та реагувати на неї
'''






note_list = [] 
note_file = "notes.txt"

# Hello note; 04.07.2024 20:15

welcome_banner = '''
 __    __            __                                      __                    __     
/  |  /  |          /  |                                    /  |                  /  |    
$$ |  $$ |  ______  $$ |  ______    ______    ______        $$ |____    ______   _$$ |_   
$$ |__$$ | /      \ $$ | /      \  /      \  /      \       $$      \  /      \ / $$   |  
$$    $$ |/$$$$$$  |$$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |      $$$$$$$  |/$$$$$$  |$$$$$$/   
$$$$$$$$ |$$    $$ |$$ |$$ |  $$ |$$    $$ |$$ |  $$/       $$ |  $$ |$$ |  $$ |  $$ | __ 
$$ |  $$ |$$$$$$$$/ $$ |$$ |__$$ |$$$$$$$$/ $$ |            $$ |__$$ |$$ \__$$ |  $$ |/  |
$$ |  $$ |$$       |$$ |$$    $$/ $$       |$$ |            $$    $$/ $$    $$/   $$  $$/ 
$$/   $$/  $$$$$$$/ $$/ $$$$$$$/   $$$$$$$/ $$/             $$$$$$$/   $$$$$$/     $$$$/  
                        $$ |                                                              
                        $$ |                                                              
                        $$/                                                               
'''


commands = '''
1) exit  - to exit the app
2) add_note - to add a new note
3) print_note [i] - to print note number i
4) print_all - to print all notes   
5) help - to print this menu
'''

def add_new_note(note_text) -> bool:
    note_creation_date = datetime.today()
    note_list.append({"text": note_text, "creation_date": note_creation_date})
    return True

def print_note(index: int):
    note = note_list[index]
    # 19.12.2024 20:15 dd.mm.yyyy hh:mm
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'"{note["text"]}"\n- Created on {formatted_creation_date}\n')

def print_all_notes():
    for note_index in range(len(note_list)):
        print_note(note_index)

def save_notes():
    with open(note_file, 'w') as file:
        for note in note_list:
            file.write(f'{note["text"]};{note["creation_date"]}\n')

def read_notes() -> list[dict]:
    note_list = []
    with open(note_file) as file:
        for line in file:
            text, date = line.strip().split(';')
            creation_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            note_list.append({"text": text, "creation_date": creation_date})
    return note_list


def init():
    global note_list
    note_list = read_notes()

    print(welcome_banner)
    print("\nHello and welcome to our app!\n")
    print(commands)
    print()

def main():
    while True:
        command, *args = input('Please enter command (enter exit to stop): ').strip().split(' ') # print_note 1  add_note
        if command == 'exit':
            print("GoodBye!")
            save_notes()
            break
        elif command == 'add_note':
            text = input('Please, enter note text: ')
            if add_new_note(text):
                print('\nNote added successfully.\n')
            else:
                print('\nError while adding a note.\n')
        elif command == 'help':
            print(commands)
        elif command == 'print_note':
            index = int(args[0]) - 1
            if index < 0 or index >= len(note_list):
                print("Please enter a valid note number.")
                continue
            print_note(index)


# text = input("Enter ur notation: ")
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)

init()
main()


        



# print_all_notes()
