#! python3
from flask import Flask, render_template, url_for, request, jsonify, redirect, flash
from flask import make_response
import pprint
import time
import random
food_dict = {}
last_dict = {}
app = Flask(__name__)

food_dict = {}
food_dict = {'B4:21:8A:F0:13:44': {'type': 'orange', 'price': 8}}
last_dict = {}
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
        return pprint.pformat(all_data)
    if request.method == 'POST':
        file = open('data.txt', 'a+', newline="\n")
        temp = request.form.get('temp')
        mac = request.form.get('mac')
        timestamp = time.time()
        htime = time.ctime(timestamp)
        sensor_id = request.form.get('id')
        #price = food_dict[mac]['price']
        price = 10
        json_data = {'mac': mac, 'sensor_id': sensor_id,
                     'temp': temp, 'timestamp': int(timestamp), 'time': htime, 'price': price}
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
    return last_price()


def last_price():
    global food_dict
    global last_dict
    food_dict[last_dict['mac']]['price'] = food_dict[last_dict['mac']
                                                     ]['price'] - (float(last_dict['temp']) * 0.0005)
    price_ = float("%0.2f" % food_dict[last_dict['mac']]['price'])
    return str(price_)


if __name__ == '__main__':
    food_dict = {'B4:21:8A:F0:13:44': {'type': 'orange', 'price': 8}}
    cprice = 0
    app.run()
