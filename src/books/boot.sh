#!/bin/bash
flask seeding 1000
exec gunicorn -b :5000 "app:create_app()"
