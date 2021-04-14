## Repositorio ejercicio SignUp y Login con HTML y Python Flask desde cero
**Instalación:**

Requiere los paquetes de: 
*pip install Flask*
*pip install flask-sqlalchemy*
*pip install PyMySQL*
*pip install passlib*

## Entrando a la base de datos:

*mysql -u root -h localhost*

Luego de esto:
*Create a database called register*

*USE register;*

*create table users(id SERIAL PRIMARY KEY, name varchar (50) not null, email varchar (50) not null, password varchar (300));*

*show tables;*
*describe users;*

#### Ejecuta el ejercicio con python app.py