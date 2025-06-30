def to_do_list():
    task = []
    print("------To Do List------")
    task_count = 0
    while True:
        print("Enter the choice : \n1)Add task  2)Update task  3)Delete task  4)Show task  5)Exit")
        choice = int(input("Enter the choice : "))

        #Adding a task
        if choice == 1:
            add_task = input("\nEnter task you want to add : ")
            task.append(add_task)
            print("Task added successfully...\n")
            task_count = task_count + 1
        
        #updating a task
        elif choice == 2:
            if task == []:
                print("\nOops! there is no tasks to update, the list is empty\n")     
            else:
                update = int(input("\nEnter a task number to update : "))
                if update > task_count:
                    print("\nEnter a valid number\n")
                else:
                    task[update - 1] = input("Enter new task : ")
                    print("Task updated successfully...\n")
        
        #Deleting a task
        elif choice == 3:
            if task == []:
                print("\nOops! there is no tasks to delete, the list is empty\n")     
            else:
                delete = int(input("\nEnter a task number to delete : "))
                if delete > task_count:
                    print("\nEnter a valid number\n")
                else:
                    del task[delete - 1]
                    print("Task deleted successfully...\n")

        #showing a task
        elif choice == 4:
            if task == []:
                print("\nOops! there is no tasks to Show, the list is empty\n")
            else:
                j = 1
                print()
                for i in task:
                    print(f"{j}. {i}")
                    j = j + 1
                print()

        #Exiting the program
        elif choice == 5:
            print("Program Exited...")
            break

        #Invalid number
        else:
            print("\nEnter a valid choice...\n")

to_do_list()