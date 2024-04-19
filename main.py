
while True:
    user_action = input("Type 'add', 'edit', 'del', 'show' or 'exit':").lower()
    match user_action:
        case 'add':
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.append(input("Enter todo:").title() + "\n")
            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'edit':
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            print("Your todos are:", todos)
            index = int(input("Enter index to edit:"))
            new_todo = input("Enter new todo:").title()
            todos[index] = new_todo
            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'del':
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            print("Your todos are:", todos)
            index = int(input("Enter index to delete:"))
            todos.pop(index)
            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            print("Your todos are:")
            file_lines = open("files/todos.txt", "r").readlines()
            for index, todo in enumerate(file_lines):
                print(f"{index}. {todo}")
        case 'exit':
            break
        case _:
            print("Invalid choice")
