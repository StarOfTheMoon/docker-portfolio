# docker-portfolio
My portfolio on docker

Portfolio dockerized in Django/Postgres
Custom image : docker.io/starofthemoon/portfolio:1.1

## Run the project
```docker-compose up```

## Set parameters for postgres connection (if needed)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
## migrate all tables on postgres (after the first launch)
```
docker-compose exec web python manage.py migrate
```

##  create a super user for django administration
```
docker-compose exec web python manage.py createsuperuser
```

## Run a command on the project
```docker-compose run --rm web COMMAND``` 
OR
```docker-compose exec web COMMAND```

## Remove container project and database
```docker-compose down```

