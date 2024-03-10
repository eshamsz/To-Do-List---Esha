import time 
from functions import read_todo, write_todo
prompt = "Enter a to-do:"
invalid_msg = "An Invalid Command Has Been Entered"
todo_list = []

while True:
    
    action = input("type add [action], show, edit, complete or exit: ")
    action = action.strip()
        
    if action.startswith('add'):
        todo = action[4:] # slice out add 

        todo_list = read_todo()

        todo_list.append(todo.title() + '\n') 

        write_todo(todo_list)
    
    elif action.startswith('show'):
        
        todo_list = read_todo()
        
        for index, item in enumerate(todo_list):
            row = f"{index + 1}-{item.strip("\n")}"
            print(row)
    
    elif action.startswith('edit'):
        try:
            number = int(action[5:]) - 1

            todo_list = read_todo()
            
            new_todo = input("Enter new todo: ") + '\n'
            todo_list[number] = new_todo.title()

            write_todo(todo_list)
        except ValueError:
            print(invalid_msg)
            continue

    elif action.startswith('complete'):
        try:    
            number = int(action[9:])

            todo_list = read_todo()

            todo_list.pop(number-1)

            write_todo(todo_list)
        except IndexError:
            print("There is no item with that number")
            continue

    elif 'exit':
        break
    
    else:
        print(invalid_msg)

print("Good luck")