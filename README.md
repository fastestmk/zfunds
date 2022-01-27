# Setup

- Clone the repo using `git clone https://github.com/fastestmk/zfunds` 
- Create virtual environment using virtualenv library using `virtualenv -p python env`
- cd to the project `cd/zfunds` and install requirements using `pip install -r requirements.txt`
- Setup a database using postgres https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e
- Create same database setting in settings.py file in zfunds/settings.py
	```
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': "DATABASE_NAME", # use database name that you defined in postgres
	        'USER': "USER", # user name of database 
	        'PASSWORD': "PASSWORD",
	        'HOST': "localhost",
	        'PORT': '5432',
	    }

	}
	```
	

- Enter your email credential in settings.py file
	```
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_USE_TLS = True
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_PORT = 587
	EMAIL_HOST_USER = "EMAIL_HOST_USER" # Please put your gmail and also removing security from that email https://www.google.com/settings/security/lesssecureapps
	EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD' # Use your gmail password
	```

- Setup a slack channel to send notification to user https://howchoo.com/python/python-send-slack-messages-slackclient	
- Put slack token in settings.py file
  `
  	SLACK_TOKEN = "SLACK TOKEN"
  `

- Create superuser to test the notification module
	`
		python manage.py createsuperuser 
	`

- Run the server using `python manage.py runserver`

- To login, put this url http://127.0.0.1:8000/api/token/ into postman with payload 
	```
		{
		    "username": "username",
		    "password": "password"
		}
	```

	get token from "access" key in repsonse of this url and login using http://127.0.0.1:8000/users/api/user/ by putting token into Authorization tab in postman with Bearer Token and hit the api

- Send notification to user with http://127.0.0.1:8000/notifications/send-notification/ (user must be logged in)










	