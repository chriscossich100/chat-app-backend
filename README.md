# Backend side of Cossich Chat App

This is the backend side of the Cossich Chat App

# Welcome to my Chat App
  

## Getting Started

This server should start working in just a few steps:

****First things first! lets create a virtual environment:****
If not already installed, install the virtual environment in the main directory which is also where the manage.py file is located.
(python3 command)
`python3  -m  pip  install  --user  virtualenv`

Now with this, we can create a virutal environment:
`python3  -m  venv  env` the *env* is the name of the virtual environment. You can change this. However, env is mostly used and easy to tell that its a virtual environment.

Once the virtual environment has been created, activate it. To install dependencies and future dependencies for this project, its best to stay in the virtual environment.
`source env/bin/activate` 

**Installing all the dependencies**
Provided in the project, is a requirements.txt file, This file contains all the dependencies used in this project. They will need to be installed. 
 
 ````
python3 -m pip install -r requirements.txt
````

Now you have all the dependencies installed. Some of these dependencies are: 

 - Django (*Main dependency needed to run the project*)
 - Gunicorn (*If deploying to heroku, the procfile will need to specify this* At the end I will explain this part)
 - python-dotenv (*package that is used to set up environmental variables*)
 - Django Rest Framework (*Another main package needed to set up the API routes.*)
 - Psycopg2 (*Postgres Database*)

 
**Modifying the Settings.py File**
Not much needs to be changed here: The project uses postgres. However, it uses a custom db set on my machine. This means if you have postgres, you will need to create a database and connect it to the settings file (steps on how to do that will come up). If you plan on keeping this app on your local machine you can easily use the standard db.sqlite db provided by django. 

When taking a look at the settings.py file I've provided, you will notice that there are environmental variables associated to it. Of course, you wont need this if you plan on keeping this project in development and not deploy it. If you do plan on keeping this in dev, simply replace the values of the current settings.py file with what is provided below. If interested in using environmental variables skip to the **setting environmental variables part**

*steps on how to use sqlite:*
on the settings file configure the DATABASE to have these values:

    DATABASES = { 
	    'default': {
		    'ENGINE': 'django.db.backends.sqlite3',
		    'NAME': BASE_DIR / 'db.sqlite3'
	    }
	}
	
*Steps  on how to configure the database to use postgres and not environmental variables:*

    DATABASES = {
	    'default': {
			'ENGINE': 'django.backends.postgresql_psycopg2,
			'NAME': 'name of your database', #ex: mydatabase
			'USER': 'username associated with that database', #ex: chriscoss95
			'PASSWORD': 'password used to access the database', #ex: 12234Password!
			'HOST': 'name of the host (in this case if this is in your local machine it should be 'localhost')', #ex: localhost
			'PORT': 'Port number. By default, postgres assigns the port as 5432'
		}


**Setting Environmental Variables**
This step is very helpful when using different variables depending on whether you're in production or development. Of course, if you plan on using a database thats already connected to host provider for development and production, you can just set the values in the settings.py file. If you want to use different variables (different url routes, different databases) for dev or prod, we can set environmental variables. It's quite easy to do:

**Creating .env file**
First, we will need to create a .env file. The .env file needs to be created in the main directory of the project (same location as the manage.py file). In the .env file, we will set the values configured in the settings.py file:

````
DB_NAME=name of your database #no quotes
DB_USER=username associated with the database #no qoutes
DB_PASSWORD=password of the database #no quotes
DB_HOST = name of the host #no quotes
DB_port = 5432 
  ````


**Updating the settings.py file to include different hosts**
This part is only necessary if you decide to deploy this app and the frontend side to hosting providerS. In the settings.py file you will notice that there is a configured variable called ALLOWED_HOSTS. It contains localhost server, the frontend url and the backend server url (just include it to be safe). The front-end if deployed to a host provider, will need to communicate to the backend so on the .env file you can set the value ALLOWED_HOSTS_FRONTEND to the url of your app provided by your host provider (Ex. If the application is hosted on vercel, get the url and set it to the env variable). So now, the application knows that it can take requests from that url. You can do the same for ALLOWED_HOSTS_BACKEND. 

**One Last Step**
these environment variables are actually just used for development. So technically when running the code on the local machine, it will use the variables that you set in the .env file. If you use a host provider to deploy the backend and want to use a seperate database (these can be provided by your host provider) we will need to set up the same env variables through your host provider. Depending on the host provider, accessing this part is different, once you know the location of where to insert these env variables you will do something like this: 
````
DB_NAME = name of the provided database or different database to be used in production
DB_USER = username of the provided database or different database to be used in production
````
*THE SAME APPLIES FOR: password, hosts, and port*


**Quick info about deploying with Heroku**
If deploying with heroku, usually apps require a file called Procfile. You can read about it on their site. There is one provided here. If you do plan on changing the project structure, including the name of the project make sure to change the name in the Procfile as well.