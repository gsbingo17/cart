from flask import Flask, request, jsonify
from order_service import create_order, list_orders
import uuid
import os
import json
import google.cloud.logging
import logging

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def create_order_route():
    """
    Create a new order.
    """

    # --- Print the entire request object ---
    print(request)  

    # --- Print specific attributes ---
    print("Request Method:", request.method)
    print("Request Headers:", request.headers)
    print("Request JSON Data:", request.get_json()) 
    data = request.get_json()
    items = data.get('items')
    if not items:
        return jsonify({'error': 'no items'}), 400
    order = create_order(items)
    return jsonify({
        'order_id': order['order_id']
    })

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  app.run(debug=True, host="0.0.0.0", port=port)
