import csv
from flask import Flask
from flask import jsonify

filename='iris.csv'
raw_data = open (filename , 'r')
reader = csv.reader ( raw_data, delimiter =",", quoting = csv.QUOTE_NONE)
x = list (reader)

app = Flask(__name__)

@app.route('/json')
def show_list():
    return jsonify(x)
        
if __name__ == '__main__':
    app.run()