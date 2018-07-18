import json

from flask import (Blueprint, jsonify, request)

from pricing_service.api.models import Product, VATBand

api = Blueprint('api', __name__)


def product_lookup(all_products, product):
    product_id = product.get('product_id', 0)
    product_obj = all_products.get(product_id)
    return product_obj


def product_sub_total(price, quantity):
    return round(price * quantity)    


def vat_band(vatband, price):
    return round(price * vatband.rate)


@api.route('/products', methods=['POST'])
def post_products():
    all_products = {product.id: product for product in \
                    Product.query.all()}
    data = request.json
    response_data = {}
    prices = []
    price_total = 0
    vat_total = 0
    for product in data['order']['items']:
        product_obj = product_lookup(all_products, product)
        sub_total = product_sub_total(product_obj.price, product['quantity'])
        vat = vat_band(product_obj.vatband, sub_total)
        price_total += sub_total
        vat_total += vat
        prices.append({'product_id': product_obj.id,
                       'sku': product_obj.sku,
                       'name': product_obj.name,
                       'quantity': product['quantity'],
                       'price': sub_total,
                       'vat': vat, 
                       'vat_band': product_obj.vatband.name})
 
    response_data['prices'] = prices
    response_data['totals'] = {'vat': vat_total, 'price': price_total}
    response_data['vat_bands'] = {band.name: band.rate for band in \
                                  VATBand.query.all()}
    return jsonify(response_data)
