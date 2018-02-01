# docker-portfolio
My portfolio on docker

Portfolio dockerized in Django/Postgres

Custom image : docker.io/starofthemoon/portfolio:1.1

Interface to view database : adminer


## Install
### Clone the project and follow instructions
Clone the project
``` 
git clone https://github.com/StarOfTheMoon/docker-portfolio
```
go on the directory
```
cd docker-portfolio
```
build and run the project
```
docker-compose up 
```
Do migrations for set tables on database
```
docker-compose exec web python manage.py migrate
```
Create a super user for django admin
```
docker-compose exec web python manage.py createsuperuser
```
Set parameters for postgres connection (if needed)
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
Run the project and enjoy
```
docker-compose up 
```
You can access with your local adresses with thoses ports : 

| Server  | Port |
|---------|------|
| Django  | 8000 |
| Adminer | 8080 |

---------------------------------------------------------------------------------------------
## Commands
### Set/Run the project
``` 
docker-compose up 
```

### migrate tables on changes
```
docker-compose exec web python manage.py migrate
```

###  create a super user for django administration
```
docker-compose exec web python manage.py createsuperuser
```

### Run a command on the project
```docker-compose run --rm web COMMAND``` 
OR
```docker-compose exec web COMMAND```

### Remove container project and database
```
docker-compose down
```

### Ports 

| Server  | Port |
|---------|------|
| Django  | 8000 |
| Adminer | 8080 |


