# DimensionDash Django Web Application

## Setup
First, clone the repository:
```
git clone https://github.com/nickconnors/DimensionDash/
cd DimensionDash
```

**Optional**, but recommended step: create Python virtual environment.

Next, install dependencies. In this application, the only dependency is Django:
```
pip install Django
```

Apply the database migrations:
```
cd project
python manage.py makemigrations
python manage.py migrate
```

Add '127.0.0.1' (or your desired host IP) to ALLOWED_HOSTS in settings.py:
```
cd project
nano settings.py
```

## Running the Application
To run the applicarion, run the following command from the first project folder:
```
python manage.py runserver
```

Enter 'http://127.0.0.1:8000/' in your browser (or your other specified allowed host
