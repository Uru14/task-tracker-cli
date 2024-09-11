import argparse
import json
import os
from datetime import datetime


def load_task():
    if not os.path.exists('task.json'):
        return []
    try:
        with open('task.json', 'r') as file:
            if file.read().strip() == '':
                return []  
            file.seek(0) 
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: El archivo JSON está dañado o contiene un formato no válido.")
        return []

    
def save_tasks(tasks):
    with open('task.json','w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_task()

    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea añadida: {description} (ID: {new_task['id']})")

def update_task(task_id, new_description):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task {task_id} not found")

def delete_task(task_id):
    tasks = load_task()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully.")


def mark_task(task_id, status):
    valid_statuses = ['todo', 'in-progress', 'done']
    if status not in valid_statuses:
        print(f"Invalid status: {status}. Valid statuses are: {valid_statuses}.")
        return
    
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task {task_id} not found.")

def list_tasks(status=None):
    tasks = load_task()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('description', help='Descripción de la tarea')

    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('task_id', type=int, help='ID de la tarea a actualizar')
    update_parser.add_argument('description', help='Nueva descripción de la tarea')

    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('task_id', type=int, help='ID de la tarea a eliminar')

    mark_parser = subparsers.add_parser('mark')
    mark_parser.add_argument('task_id', type=int, help='ID de la tarea a marcar')
    mark_parser.add_argument('status', help='Estado de la tarea (todo, in-progress, done)')

    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('status', nargs='?', help='Estado de las tareas a listar (todo, in-progress, done)')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.task_id, args.description)
    elif args.command == 'delete':
        delete_task(args.task_id)
    elif args.command == 'mark':
        mark_task(args.task_id, args.status)
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
