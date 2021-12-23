#PyCharm
No PyCharm para acessar o documento importado basta segurar Ctrl + botão esquerdo.
Isso funciona em virtualenv ou em versões pro da IDE que deem suporte ao docker-compose. Se for utilizado o docker-compose manualmente essa função não encontrará os arquivos.

#Migrations
Antes da versão 1.0 os arquivos da(s) pasta(s) migrations estarão em .gitignore, exceto pelo(s) ```__init__.py```


#Comandos importantes

##Docker
###Iniciar
```
docker-compose up
```
###Resetar:
```
docker stop $(docker container ls -a -q)
docker rm $(docker container ls -a -q)
docker rmi $(docker image ls -a -q -f since=<postgres id>)
docker volume rm $(docker volume ls -q)
```
####Se necessário, usar:
```
docker system prune -a -f --volumes
```
####Executar container python no terminal (bash):
```
docker exec -it sistemasisu_web_1 bash
```
##Django
```
django-admin startproject <projeto>
django-admin startapp <app>
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```

