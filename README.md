# Overview

As an aspiring software engineer, my goal for this project was to master the fundamentals of backend web development and routing by building a dynamic web application from scratch. 

This project is a Portfolio Web Application designed to showcase my programming work. It features a responsive layout and dynamic content generation. To start the local test server for this application, open a terminal in the root project directory, activate the virtual environment, and run the command `python manage.py runserver 8080`. Once the server is running, open a web browser and navigate to `http://127.0.0.1:8080/` to see the home page.

The purpose of writing this software was to gain hands-on experience with the Django web framework. Specifically, I wanted to learn how to manage project structures, configure URL routing, connect Python backend views to frontend HTML templates, and securely handle HTTP POST requests from user input.

[Software Demo Video](https://youtu.be/G7mFp43DrZw)

# Web Pages

The web application transitions between pages using Django's URL dispatcher (`urls.py`), which maps specific URL paths to Python functions (views). These views then render the appropriate HTML templates for the user. 

* **Home Page (`/`)**: A clean landing page that welcomes the user and provides a call-to-action button to view my work. It dynamically inherits its navigation bar and core styling from a parent `base.html` template.
* **Projects Gallery (`/projects/`)**: This page acts as a portfolio gallery. It dynamically generates Bootstrap cards by iterating through a Python list of dictionaries passed from the backend view, rendering the title and description of each project using a Jinja `{% for %}` loop.
* **Contact Page (`/contact/`)**: An interactive form allowing users to reach out. When a user submits their name (a POST request), the backend intercepts the data and dynamically injects a personalized success message back into the re-rendered HTML page.

# Development Environment

* **IDE:** Visual Studio Code
* **Version Control:** Git & GitHub
* **Command Line:** macOS Terminal 

* **Programming Language:** Python 3.9
* **Web Framework:** Django 4.2
* **Frontend:** HTML5, CSS3, and Bootstrap 5 (imported via CDN for responsive styling)

# Useful Websites

* [Django Official Documentation: Writing Views](https://docs.djangoproject.com/en/4.2/topics/http/views/)
* [Bootstrap 5 Documentation: Cards and Forms](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Python Docs: Creation of Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

# Future Work

* Integrate an SQLite database to store and retrieve portfolio projects rather than using hardcoded Python lists in the view file.
* Add a secure administrative dashboard (`/admin`) to easily create, update, and delete project entries without altering the codebase.
* Implement form validation and email routing on the Contact page so submitted messages are automatically forwarded to my personal email inbox.