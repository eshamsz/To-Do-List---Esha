import streamlit as sl
import functions

todo_list = functions.read_todo()

def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todo_list.append(todo)
    functions.write_todo(todo_list)

def complete_todo():
    todo_list.remove(complete_todo)
    functions.write_todo(todo_list)

sl.title("My Todo App")
sl.subheader("An app to UP your productivity!")
sl.write("Made By: Esha Saleem")

for index, todo in enumerate(todo_list):
    item = sl.checkbox(todo, key=todo)
    if item:
        todo_list.pop(index)
        functions.write_todo(todo_list)
        del sl.session_state[todo]
        sl.rerun()  

sl.text_input(label="", placeholder="Enter a todo item...",
              on_change=add_todo, key='new_todo')