#!/usr/bin/env bash
export FLASK_APP=flask_app/server.py
flask db init
flask db migrate -m 'init'
flask db upgrade
flask run --host=0.0.0.0