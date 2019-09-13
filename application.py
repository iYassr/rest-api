#! python3 
from flask import Flask, render_template, url_for, request, jsonify, redirect, flash
from flask import make_response
import time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        file = open('data.txt','r', newline="\n")
        all_data = file.read()
        print(all_data)
        file.close()
        return all_data
    if request.method == 'POST':

        file = open('data.txt','a+', newline="\n")
        temp = request.form.get('temp')
        file.write('\ntemp: {}, timestamp: {}'.format(temp,time.time()))
        file.close()
        return ''

@app.route('/data/<int:temp>', methods=['GET'])
def submit(temp):
    if request.method == 'GET':
        file = open('data.txt','a+', newline="\n")
        file.write('\ntemp: {}, timestamp: {}'.format(temp,time.time()))
        file.close()
        return ''




if __name__ == '__main__':
    app.run()
