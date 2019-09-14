import requests
import time

requests.post('https://fask-api.azurewebsites.net', data = {'temp':'20','mac':'B4:21:8A:F0:13:44','sensor_id':'example_sensor_id'})
