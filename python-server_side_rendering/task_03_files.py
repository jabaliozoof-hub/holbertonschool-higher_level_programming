#!/usr/bin/python3
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template('product_display.html',
                               error='Wrong source')

    try:
        data = read_json() if source == 'json' else read_csv()
    except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
        return render_template('product_display.html',
                               error='Error reading data file')

    if product_id is not None:
        try:
            pid = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error='Product not found')
        data = [p for p in data if p['id'] == pid]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
