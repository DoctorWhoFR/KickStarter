# QStarter
[![N|Solid](https://img.shields.io/badge/docker%20build-automated-066da5?style=for-the-badge)](https://nodesource.com/products/nsolid) [![N|Solid](https://img.shields.io/github/license/DoctorWhoFR/KickStarter?style=for-the-badge)](https://nodesource.com/products/nsolid)


👀 **QStarter is a starter project for my current personnel project of an KickStarter application with customs features.
That is the public repo of the api and other file included with all DockerFile and docker-compose.**

/!\ YOU DONT NEED TO HAVE DOCKER OR DOCKER-COMPOSE FOR NOW /!\

# POSTMAN DOCUMENTATION API
All informations you need are on this postman documentation:
https://documenter.getpostman.com/view/2899395/SWE3czHV?version=latest

# With docker 
If you use docker you just have to make:
```bash
docker-compose build
docker-compose run
```

## Usage:
*Refer to postman documentation api for route instruction.*

### SERVER AUTHENTIFICATION API *[DEFAULT RUN PORT: 5001]*

### SERVER PROJETS API *[DEFAULT RUN PORT: 5000]*

# Without Docker

## Installation

To work with the api we need to install all needed dependencies:

```bash
pip install flask
pip install flask_restful
pip install sqlalchemy
pip install redis
pip install simplejson
```

## Usage
Run server api command:

### PROJETS API *[PORT: 5000]*: 
```python
python projets_api/main.py
```

### AUTHENTIFICATION API *[PORT: 5001]*: 
```python
python projets_api/main.py
```
You can also seed the database with realy dump data with
```python
python seeder.py
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

