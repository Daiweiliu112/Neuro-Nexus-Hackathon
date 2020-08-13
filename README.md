# Gamifying_Mental_Health

##### BINOY’s
Had trouble initially deploying locally on Windows OS → 18.04 Ubuntu OS VM
Created a local virtualenv, external the repo
pip install --upgrade -r requirements.txt
Gets stuck on psycopg2==2.8.4, so before running pip install:
sudo apt-get update
sudo apt-get install libpq-dev python-dev
To setup the database:
sudo apt-get install libpq-dev python-dev (which you already ran)
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql ### to enter the psql shell as user postgres
CREATE DATABASE dbname;
\list  ### verfiy
ALTER USER user_name WITH PASSWORD 'new_password';
Node (v8.10.0) 
Npm
sudo npm -g install npm@6.11.3


Sudo docker system prune --volumes --force

##### EDEN’s

Tested in 18.04 Ubuntu OS

Install Docker
https://docs.docker.com/engine/install/ubuntu/  

Install Docker-Compose
https://docs.docker.com/compose/install/#install-as-a-container  

Run the following commands to spin up containers

```shell
docker-compose up -d --build
```

Check individual container logs with the following command:

```shell
docker-compose logs -f '<container-name>'
```

Run individual django commands:

```shell
docker-compose exec web python manage.py my_custom_command
```

Create superuser:

```shell
docker-compose exec web python manage.py createsuperuser
```



