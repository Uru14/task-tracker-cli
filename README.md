# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. Built with Python, this tool allows you to add, update, delete, and list tasks in a JSON file.

## Descripción

Task Tracker CLI es una aplicación que te ayuda a gestionar tus tareas diarias a través de la línea de comandos. Puedes añadir nuevas tareas, actualizar o eliminar tareas existentes, marcar tareas como en progreso o completadas, y listar todas las tareas o filtrar por estado (pendientes, en progreso, completadas). La información de las tareas se guarda en un archivo JSON en el directorio actual.

## Características

- Añadir nuevas tareas
- Actualizar tareas existentes
- Eliminar tareas
- Marcar tareas como en progreso o completadas
- Listar todas las tareas
- Filtrar tareas por estado: completadas, pendientes, en progreso

## Requisitos

- Python 3.x

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/Uru14/task-tracker-cli.git
   cd task-tracker-cli

2. **Crea un entorno virtual (opcional pero recomendado)**:

    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

3. **Ejecuta el programa directamente con Python**:

    python3 task_tracker.py <comando> <argumentos>

    Donde <comando> puede ser add, update, delete, mark-in-progress, mark-done, list, list done, list todo, list in-progress, etc.
    
4. **Ejemplo de uso**:

    python3 task_tracker.py add "Comprar leche"
    python3 task_tracker.py list