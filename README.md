# QKickstarter

QKickstarter is a starter project for my current personnel project of an KickStarter application with customs features.
That is the public repo of the api and other file included with all DockerFile and docker-compose.

/!\ YOU DONT NEED TO HAVE DOCKER OR DOCKER-COMPOSE FOR NOW /!\

#Without Docker

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

To run the server execute this command
```python
python main.py
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
