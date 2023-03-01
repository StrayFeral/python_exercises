Flask simple REST API exercice
==============================

This exercice is fully functional as per the specification described here.


BUILD AND RUN
=============
sudo docker build . --tag=flaskrestapp

sudo docker run flaskrestapp

Point your browser to port 5000 of the container IP to see the application is alive.

Use a REST client to play with the app.


TESTED ON
=========

PLATFORM: Lubuntu 22.04.2 LTS, Docker version 23.0.1, build a5ee5b1

CONTAINER (Dockerfile included): ubuntu:20.04, Python 3.8.10, Flask 2.2.2, Werkzeug 2.2.2

WITH: Advanced REST Client 16.0.1


Specification
=============

This application illustrates creating REST API with Python and Flask and dockerizing it. It provides the folowing functionality: "Usage", "Get all people", "Get person details", "Insert new person", "Delete person"


Notes
=====

I started learning Flask from scratch and spent 2 days and drank 2 Monster Energy cans while learning Flask and writing this. Enjoy.
