import requests
import time

requests.post('http://localhost:5000', data = {'temp':'20','mac':'B4:21:8A:F0:13:44','sensor_id':'example_sensor_id'})

#requests.get('http://localhost:5000/data/99')
