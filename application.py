#! python3
from flask import Flask, render_template, url_for, request, jsonify, redirect, flash
from flask import make_response
import pprint
import time
import random
import json
food_dict = {}
food_dict = {'B4:21:8A:F0:13:44': {'type': 'orange', 'price': 8}}
last_dict = {}
price = 25
app = Flask(__name__)

food_dict = {}
ast_dict = {}
fake_price = 100.1
lemon = 5
orange = 8
potato = 10
avocado = 20


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        file = open('data.txt', 'r', newline="\n")
        all_data = file.read()
        file.close()
        final_str = "[ {} ]".format(all_data)
        return str(final_str)
    if request.method == 'POST':
        small_file = open('small_file.txt', 'w')
        price_file = open('price_file.txt', 'w')
        file=open('data.txt', 'a+', newline = "\n")
        temp=request.form.get('temp')
        mac=request.form.get('mac')
        timestamp=time.time()
        htime=time.ctime(timestamp)
        sensor_id=request.form.get('id')
        # price = food_dict[mac]['price']
        global price
        price=price - (float(temp) * 0.005)
        json_data={'mac': mac, 'sensor_id': sensor_id,
                     'temp': temp, 'timestamp': int(timestamp), 'time': htime, 'price': price}
        price_file.write(str(price))
        price_file.close()
        small_file.write(str(json_data))
        small_file.close()
        file.write(str(json_data))
        file.close()
        #
        last_dict['mac'] = mac
        last_dict['timestamp'] = timestamp
        last_dict['htime'] = htime
        last_dict['sensor_id'] = sensor_id
        last_dict['temp'] = temp
        last_dict['price'] = price
        return 'posted'


@app.route('/get_request', methods=['GET', 'POST'])
def get_request():
    if request.method == 'GET':
        small_file = open('small_file.txt', 'r')
        data = small_file.read()
        small_file.close()
        return str(data)
    return ''


@app.route('/data/<int:temp>', methods=['GET'])
def submit(temp):
    if request.method == 'GET':
        file = open('data.txt', 'a+', newline="\n")
        json_data = {"temp": temp, "timestamp": int(time.time())}
        file.write(str(json_data))
        file.close()
        return 'posted'


@app.route('/get_last_update', methods=['GET'])
def get_last_update():
    #   food_dict[last_dict['mac']]['price'] = food_dict[last_dict['mac']]['price']  - (float(last_dict['temp']) * 0.0005)
    #   last_dict['price'] = float( "%0.2f" % food_dict[last_dict['mac']]['price'])
    #

    #
    global last_dict
    last_dict['price'] = last_price()
    return last_dict


@app.route('/get_price', methods=['GET'])
def get_price():
    if request.method == 'GET':
        price_file = open('price_file.txt', 'r')
        data = price_file.read()
        price_file.close()
        last_data = float( "%0.2f" % float(data))
        return str(last_data)

    return last_price()


def last_price():
    global food_dict
    global last_dict
    # food_dict[last_dict['mac']]['price'] = food_dict[last_dict['mac']]['price'] - (float(last_dict['temp']) * 0.0005)
    price_ = float("%0.2f" % food_dict[last_dict['mac']]['price'])
    return str(price_)


if __name__ == '__main__':
    food_dict = {'B4:21:8A:F0:13:44': {'type': 'orange', 'price': 8}}
    cprice = 0
    app.run()
