import requests
import time

requests.post('http://localhost:5000', data = {'temp':'1','mac':'fsadfasdfasdf','sensor_id':'example_sensor_id'})

#requests.get('http://localhost:5000/data/99')
