# A sample for flask app
It is a sample of restful flask app.
- python 3.8
- postgresql
- docker runable

## How to use
1. Edit the database entities in 「flask_app/model.py」.
2. Edit the RESTful API in 「flask_app/rest.py」.
3. Execute database migration.
4. run & test.

## db migration
we use Flask-Migrate to manage database migration.
follow the steps to manage database entities:

```bash
$ expose FLASK_APP=flask_app/server.py
```
```bash
$ flask db init
```
1. change model definitions in flask_app/model.py
2. under root folder:
```bash
$ flask db migrate -m '${comment about the revision}'
```
3. apply changes to the database:
```bash
$ flask db upgrade
```

## Run & Test
### Run server (local)
postgresql in required.
Edit username and password in「config.yml」 file
```bash
$ expose FLASK_APP=flask_app/server.py
$ flask run --host=0.0.0.0
```
### Run server (Docker)
```bash
$ docker-compose up -d --build
```
stop the container
```bash
$ docker-compose down
```

