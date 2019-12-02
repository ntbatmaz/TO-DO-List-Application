#Introduction

This is a simple Todo application built off Django and React.

# Requirements
* Python3
* Pipenv

#Install
 ```[cd django-todo-react]```
 ```[pipenv install]```
 ```[pipenv shell]```
 ```[pipenv install djangorestframework]```
 ```[pipenv install django-cors-headers]```
 ```[cd frontend]```
 ```[npm install]```
 ```[cd ..]```
 

#Run 
You will need two terminals pointed to the frontend and backend directories 

 Run this command to start the backend server in the ```[backend]``` directory: ```[python manage.py runserver]``` (You have to run this command while you are sourced into the virtual environment)
 Run this command to start the frontend development server in the ```[frontend]``` directory: ```[npm start]``` (This will start the frontend on the adddress [localhost:3000](http://localhost:3000))

#Missing 
- User registration(screen complete but failed to connect)
- User login(screen complete but failed to connect)
- Each to-do item should have a deadline.
- Order to-do items on a to-do list by create date, deadline, name, or status.
#Studied and Cited Sources
https://www.youtube.com/watch?v=QAVoXJtQ9QM
https://www.youtube.com/watch?v=dkK7ZmW1klE
https://wsvincent.com/django-rest-framework-react-tutorial/
https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react