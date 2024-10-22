# order_service.py - OpenAPI service definition
import uuid
from google.cloud import firestore

db = firestore.Client(project="learning-centre-352514")
orders_ref = db.collection("orders")

def create_order(items):
    """
    Create a new order and store it.
    """
    order_id = str(uuid.uuid4())
    order = {
        'order_id': order_id,
        'items': items
    }

    # Add the order to Firestore
    order_doc_ref = orders_ref.document(order_id)  # Create a document reference
    order_doc_ref.set(order)  # Set the data in the document

    return order
