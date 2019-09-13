#! python3
from flask import Flask, render_template, url_for, request, jsonify, redirect, flash
from flask import make_response
import pprint
import time
app = Flask(__name__)


food_dict = {'B4:21:8A:F0:13:44':{'type':'orange','price':8}}
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
        food_dict[mac]['price']. = food_dict[mac]['price'] - 2
        price = food_dict[mac]['price'] 
        json_data = {'mac': mac, 'sensor_id': sensor_id,
                     'temp': temp, 'timestamp': int(timestamp), 'time': htime, 'price': price}
        file.write(str(json_data))
        file.close()
        return 'posted'


@app.route('/data/<int:temp>', methods=['GET'])
def submit(temp):
    if request.method == 'GET':
        file = open('data.txt', 'a+', newline="\n")
        json_data = {"temp": temp, "timestamp": int(time.time())}
        file.write(str(json_data))
        file.close()
        return 'posted'

fake_price = 100
@app.route('/get_price>', methods=['GET'])
def get_price():
    return fake_price = fake_price - 0.1
 

if __name__ == '__main__':
    app.run()
