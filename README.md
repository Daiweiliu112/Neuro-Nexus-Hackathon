# Tech for Teletherapy


Tested in 18.04 Ubuntu OS & MacOS Catalina 10.15

Install Docker
https://docs.docker.com/engine/install/ubuntu/  

Install Docker-Compose
https://docs.docker.com/compose/install/#install-as-a-container  

Run the following commands to spin up containers

```shell
docker-compose up -d --build
```
or
```shell
docker-compose up -d
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



