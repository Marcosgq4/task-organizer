# Task Manager

This application consists of a task manager that helps the user keep track of their taks in order of importance and how soon the due date is.

## Distinctiveness and Complexity

We did not create a task manager in any of the other projects of this course.
The fist thing that is implemented in this project is user authentication. In order to create or update any tasks the user has to register and/or sign in. While this was the case in some of the other project, this is the first one in which I had to implement that functionality on my own. Of course, the user can only see and update their own tasks.
Oce the user is authenticated, they can Add a new task, using the Add Task form. They will be prompted to add a title, description, due date and importace.
When the user adds a task, they're redirected to their active tasks page, where the new task has been added to one of the 4 tables on the page, depending on the importance category that the user assigned it. There are 4 important categories for most important, very important, important or not important. The most important tasks with the closest due date are shown at the top, while the least important tasks with the latest due date are shown at the bottom.
The user can change the importace of a task by clicking on a dropdown menu, which will update the task's location in the table accordingly.
The user can also mark the task completed or choose to delete it.
We can navigate the the completed tasks and mark any task incomplete to bring it bask to the current tasks list or chose to delete it.
The user can navigate to the deleted tasks and restore a task that has been marked deleted. If the user clicks on delete on a task that has already been deleted they will delete the task completely from the database. 

## Files in this Project

`tasks/views.py`: Contains the view functions for the Task Manager application. This is where the logic for displaying, adding, deleting, and updating tasks is defined.
`tasks/models.py`: Defines the database models, specifically the structure of the tasks and any related data.
`tasks/urls.py`: Contains the URL routing for the Task Manager app. This file maps URLs to their corresponding view functions.
`tasks/forms.py`: Defines the forms used in the project, such as the "Add Task" form.

`tasks/templates/tasks/layout.html`: Base HTML structure used throughout the app, including the common navigation bar.
'tasks/templates/tasks/task_table.html' Base HTML to create all the tables in the project. Every other html that contains tables expands from this file.
`tasks/templates/tasks/task_list.html`: The main template that displays the list of tasks to the user.
`tasks/templates/tasks/add_task.html`: This template provides a form interface for users to add new tasks. It includes fields for the task title, description, due date, and importance.
`tasks/templates/tasks/completed_tasks.html`: Displays a list of tasks that have been marked as completed by the user. This page allows users to review their completed tasks and un-mark them or move them back to the active task list.
`tasks/templates/tasks/deleted_tasks.html`: Shows a list of tasks that the user has deleted. It has functionality to either permanently remove these tasks or restore them to the main task list.
`tasks/templates/tasks/login.html`: Provides a login interface for users. Contains fields for entering a username and password, along with a link for registration.
`tasks/templates/tasks/register.html`: Contains a registration form for new users. This form likely includes fields for username, password and password confirmation.

`tasks/static/tasks/tasks.js`: JavaScript file that may contain client-side logic, such as form validation or dynamic content updates.
`tasks/static/tasks/styles.css`: Stylesheet file defining the visual appearance and layout of the Task Manager web pages.

'db.sqlite3' : Contains the project database

`README.md`: This file. Provides an overview and documentation for the project.

## How to Run the Application

Clone the repository

Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the dependencies
pip install -r requirements.txt

Run migrations
python manage.py migrate

Start the development server
python manage.py runserver

Open a web browser and navigate to `http://127.0.0.1:8000/`

## Dependencies

Django: Web framework used.
No other packages were installed.




