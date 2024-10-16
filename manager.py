def add_task(tasks_list, task_name):
    task = {"task": task_name, "completed": False}
    tasks_list.append(task)
    print(f'Task {task_name} was added successfully!')
    return

def view_tasks(tasks_list):
    print('\n To-do list: ')
    for index, t in enumerate(tasks_list, start=1):
        status = '✓' if t['completed'] else ' '
        print(f'{index}. [{status}] - {t['task']}')
    return

def update_task(tasks_list, task_index, new_task_name):
    task_index_adjusted = int(task_index) - 1
    if task_index_adjusted >= 0 and task_index_adjusted < len(tasks_list):
        tasks_list[task_index_adjusted]['task'] = new_task_name
        print(f'Task {task_index} updated to {new_task_name}!')
    else:
        print('Task index invalid')
    return

def complete_task(tasks_list, task_index):
    task_index_adjusted = int(task_index) - 1
    if task_index_adjusted >= 0 and task_index_adjusted < len(tasks_list):
        tasks_list[task_index_adjusted]['completed'] = True
        print(f'The task {tasks_list[task_index_adjusted]['task']} was completed!') 
    else:
        print('Task index invalid')   
    return

def delete_completed_tasks(tasks_list):
    for t in tasks_list:
        if t['completed']:
            tasks_list.remove(t)
    print('Completed tasks was deleted!')
    return

tasks = []

while True:
    print('\n To-do List Manager Menu:')
    print('1. Add task')
    print('2. View tasks')
    print('3. Update task')
    print('4. Complete task')
    print('5. Delete completed tasks')
    print('6. Exit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        task_name_add = input('Enter the name of the task you want to add: ')
        add_task(tasks, task_name_add)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        view_tasks(tasks)
        task_index_update = input('Enter the number of the task you want to update: ')
        new_task_name_update = input('Enter the new name of the task: ')
        update_task(tasks, task_index_update, new_task_name_update) 
    elif choice == '4':
        view_tasks(tasks)
        task_index_complete = input('Enter the number of the task you want to complete: ')
        complete_task(tasks, task_index_complete)
    elif choice == '5':
        delete_completed_tasks(tasks)
        view_tasks(tasks)
    elif choice == '6':
        break
print("Program finished")