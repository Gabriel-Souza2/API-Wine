from flask import Flask, make_response, jsonify, request

from wine import Wine

app = Flask(__name__)

wine = Wine()

@app.route('/', methods=['GET'])
def get_all_products():

   return make_response(jsonify(wine.get_all()))

@app.route('/products', methods=['GET'])
def get_products_pagination():
    page = 1
    limit = 10
    args = request.args
    for parameter, value in args.items():
        if (parameter == 'page'):
            page = int(value)

        if (parameter == 'limit'):
            limit = int(value)

    products = wine.paginate(page, limit)

    return make_response(jsonify(products))

app.run()