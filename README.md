# To-Do List App Using Python

## Overview
A simple, yet effective To-Do List application developed using Python. This application allows users to manage their tasks by performing basic CRUD (Create, Read, Update, Delete) operations. The app stores tasks persistently in a text file, so the data is not lost when the application is closed.

### Features:
- **Add Tasks**: Allows users to add new tasks.
- **View Tasks**: Users can view all existing tasks.
- **Edit Tasks**: Users can modify the content of any task.
- **Delete Tasks**: Users can delete tasks from the list.
- **Persistent Storage**: Tasks are saved to a text file, ensuring they remain even after closing the app.

## Technologies Used
- **Python**: Core language used for developing the application.
- **File Handling**: Tasks are stored in a simple text file, making it easy to access and modify the list.
- **Data Structures**: Utilizes lists and basic CRUD operations.

## How It Works
1. **Add a Task**: Users input a new task, which gets added to the task list and saved to a text file (`tasks.txt`).
2. **View Tasks**: Displays all the tasks stored in the text file.
3. **Edit a Task**: Users can select a task by number and edit its content.
4. **Delete a Task**: Users can select a task by number and delete it from the list.

### File: `tasks.txt`
The app stores tasks in a text file (`tasks.txt`) located in the same directory as the Python script. Each task is saved on a new line.

## Getting Started

### Prerequisites
- **Python 3.x** should be installed on your machine.
  
  You can download it from the official [Python website](https://www.python.org/downloads/).

### Installation

1. Clone or download this repository to your local machine.

   ```bash
   git clone https://github.com/StackByAli/ToDoList-App-Using-Python.git
   
2. Navigate to the project directory:
   cd ToDoList-App-Using-Python

3. Run the Python script to start the app:
   python todo_list.py

**Usage**
Once the app is running, you’ll be prompted with a simple menu offering the following options:

View Tasks: Displays the current list of tasks.

Add Task: Prompts the user to enter a new task.

Edit Task: Allows the user to select a task to edit.

Delete Task: Prompts the user to delete a task by selecting its number.

Exit: Closes the app.

**Example Usage**
To-Do List App
1. View Tasks
2. Add Task
3. Edit Task
4. Delete Task
5. Exit

Choose an option: 1

To-Do List:
1. Buy groceries
2. Finish homework
3. Call mom

**Code Structure**
=> todo_list.py: The main Python script that handles the functionality of the app (adding, viewing, editing, and deleting tasks).
=> tasks.txt: A text file where the tasks are stored. Each task is written on a new line.

Developed by: Ali Raza
GitHub: @StackByAli


