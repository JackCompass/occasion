# Occasion

A Django-based web app to manage your events. After logging in, a user can:
- Create Events with title, description, image, location and date
- Favorite other events and view them on a separate page

Demo: https://youtu.be/WLkipKlNTy0

# Desktop Screen Capture
https://user-images.githubusercontent.com/22092047/131215588-f3548cc3-b92a-4820-8727-11ac37f3029f.mp4

## Desktop
![Occasion](https://user-images.githubusercontent.com/22092047/131206548-3fcf61cc-6ed0-46de-b273-79b2e09c875b.png)

## Mobile
![Ocassion Mobile 1](https://user-images.githubusercontent.com/22092047/131215389-91270bfc-3f48-4d84-a759-a3f49db35cc9.png)
![Ocassion Mobile 2](https://user-images.githubusercontent.com/22092047/131215403-0266d277-cc7f-4be8-9ac2-927174dd9c54.png)


## How to run (It's rather complicated)
1. Clone to repo to a suitable location
```
git clone https://github.com/JackCompass/occasion
```
2. Run the following pip installs
```
pip3 install django
pip3 install django-crispy-forms
pip3 install pillow
pip3 install mysqlclient
```
3. If you're on Linux, do the following apt installs:
```
sudo apt install mysql-server
sudo apt install libmysqlclient-dev
```
4. Start a MySQL interface:
```
sudo mysql -u root
```
5. Run these MySQL commands in the interface:
```
CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'UserPa$$w0rd123';
GRANT ALL PRIVILEGES ON *.* TO 'db_user'@'localhost' WITH GRANT OPTION;
CREATE DATABASE db
USE db
```
6. cd into the application code and open occasion/settings.py in the editor of your choice. Find the following configuration:
```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
	'default' : {
		'ENGINE' : 'django.db.backends.mysql',
		'NAME' : 'db',
		'USER' : '', # write your username
		'PASSWORD' : '', # write your password
		'HOST' : 'localhost',
		'PORT' : '3306',
	}
}
```
Replace with your created db username and password, so that the configuration now looks like this:
```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
	'default' : {
		'ENGINE' : 'django.db.backends.mysql',
		'NAME' : 'db',
		'USER' : 'db_user', # write your username
		'PASSWORD' : 'UserPa$$w0rd123', # write your password
		'HOST' : 'localhost',
		'PORT' : '3306',
	}
}
```

7. On terminal, run the following in order:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser # These will be your login credentials for the website
python3 manage.py runserver
```
8. Navigation to http://127.0.0.1:8000/
