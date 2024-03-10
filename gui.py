import functions
import PySimpleGUI as sg

label = sg.Text("What do you have to-do:")
input_box = sg.InputText(tooltip='Enter To-do', key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todo(), key='todo list',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App', 
                   layout=[[label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event) 
    print(values)
    match event:
            case "Add":
                todo_list = functions.read_todo()
                new_todo = values['todo'] + "\n"
                todo_list.append(new_todo)
                functions.write_todo(todo_list)
                window['todo list'].update(values=todo_list)
            case "Edit":
                edited_todo = values['todo list'][0]
                new_todo = values['todo']

                todo_list = functions.read_todo()
                index = todo_list.index(edited_todo)
                todo_list[index] = new_todo
                functions.write_todo(todo_list)
                window['todo list'].update(values=todo_list)
            case 'todo list':
                window['todo'].update(value=values['todo list'][0])
            case "Complete":
                complete_todo = values["todo list"][0]
                todo_list = functions.read_todo()
                todo_list.remove(complete_todo)
                functions.write_todo(todo_list)
                window['todo list'].update(values=todo_list)
                window['todo'].update(value='')
            case "Exit":
                break
            case sg.WIN_CLOSED:
                break
window.close()

##changes included