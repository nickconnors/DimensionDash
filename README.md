# DimensionDash Django Web Application

## Setup
First, clone the repository:
```
git clone https://github.com/nickconnors/DimensionDash/
cd DimensionDash
```

**Optional:** create Python virtual environment.

Next, install dependencies. In this application, the only dependency is Django:
```
pip install Django
```

Navigate to the main project folder and apply the database migrations:
```
cd project
python manage.py makemigrations
python manage.py migrate
```

**Optional:** add a new IP address to ALLOWED_HOSTS in settings.py from the secondary project folder:
```
cd project
nano settings.py
```

## Running the Application
To run the applicarion, run the following command from the main project folder:
```
python manage.py runserver
```

Enter 'http://127.0.0.1:8000/' in your browser (or your other specified allowed host)
