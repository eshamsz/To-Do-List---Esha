FILEPATH = "todo_list.txt"

# custom functions
def read_todo(filepath = FILEPATH):
    '''Read a text file and return a list of to-do items.'''
    with open(filepath, 'r') as file_local:
            todos_read = file_local.readlines()
    return todos_read

def write_todo(todos, filepath = FILEPATH):
    '''Wite to-do list items in the text file.'''
    with open(filepath, 'w') as file_local:
            todos_written = file_local.writelines(todos)
    return todos_written