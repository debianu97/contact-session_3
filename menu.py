tasks = []

while True:
    print("==== MY TO-DO LIST ====")
    print("Welcome to my-to-do-lit")
    print("To Add task, enter 1")
    print("To View tasks, enter 2")
    print("To Mark Task as Completed, enter 3")
    print("To Delete Task, enter 4")
    print("To Exit task, enter 5")

    choice = int(input("Please, press any number that aligns with what you will like to do: "))


    if choice == 1:
        new_task = input("Enter the name of the task")

        task = {
            "title": new_task,
            "completed": False
        }
        tasks.append(task)
        print("Task added successfuly")

    elif choice == 2:
        if not tasks:
            print("No task available")
        else:
            for task in tasks:
                print(f"Your task: {task['title']}")
                print(f"Completed: {task['completed']}")

    elif choice == 3:
        if not tasks:
            print("No task available")
            break
        else:
            for index, task in enumerate(tasks):
                print(f"{index}.{task['title']}")
        
        task_index = int(input("Enter the task number to mark as completed: "))
        tasks[task_index]["completed"] = True

        print(f"{tasks[task_index]['title']} marked as completed!")
    
    
    elif choice == 4:
        del_task = input("kindly enter the task you will like to delete")
        tasks.remove(del_task)
        print("Task Sucessfully deleted")
    
    elif choice == 5:
        print("Goodbye!")
        break
    
    else:
        print("Please enter a valid Option")

