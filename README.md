# ZipTie

Solution to the recruitment task for the position of Python Developer at ZipTie.dev.


## Quickstart

Install dependencies:
```Bash
pip install -r requirements.txt
```

Run MySQL database:
```Bash
docker run -dp 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=school mysql:9.0.1
```

Run application:
```Bash
uvicorn ziptie.main:app --app-dir src --reload
```

Behaviour tested with Python version 3.12.4.


## Configuration

Connection to database can be configured by following environment variables:
```
DATABASE_HOST        The hostname or IP to use for the connection
DATABASE_NAME        The name of the database to connect to
DATABASE_PASSWORD    The password of the database user
DATABASE_PORT        The port number to use for the connection
DATABASE_USER        The username to use for the connection
```

or directly modifying `config.py` module.
