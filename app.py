from datetime import datetime
from flask import Flask, jsonify, request
from database import User, Offer, Order, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JSON_AS_ASCII'] = False # deprecated
app.json.ensure_ascii = False
app.url_map.strict_slashes = False

db = SQLAlchemy(app)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(session.query(User).all())

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return jsonify(session.query(User).get(id))

@app.route('/users', methods=['POST', 'PUT'])
def add_user():
    data = request.json
    user = User(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        age=data.get('age'),
        email=data.get('email'),
        role=data.get('role'),
        phone=data.get('phone')
    )
    session.add(user)
    session.commit()
    return jsonify(user)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    user = session.query(User).get(id)
    session.delete(user)
    session.commit()
    return ''

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(session.query(Order).all())

@app.route('/orders/<int:id>', methods=['GET'])
def get_order_by_id(id):
    return jsonify(session.query(Order).get(id))

@app.route('/orders', methods=['POST', 'PUT'])
def add_order():
    data = request.json
    order = Order(
        name=data.get('name'),
        description=data.get('description'),
        start_date=datetime.strptime(data.get('start_date'), '%d/%m/%Y').date(),
        end_date=datetime.strptime(data.get('end_date'), '%d/%m/%Y').date(),
        address=data.get('role'),
        price=data.get('price'),
        customer_id=data.get('customer_id'),
        executor_id=data.get('executor_id')
    )
    session.add(order)
    session.commit()
    return jsonify(order)

@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order_by_id(id):
    order = session.query(Order).get(id)
    session.delete(order)
    session.commit()
    return jsonify('')

@app.route('/offers', methods=['GET'])
def get_offers():
    return jsonify(session.query(Offer).all())

@app.route('/offers/<int:id>', methods=['GET'])
def get_offer_by_id(id):
    return jsonify(session.query(Offer).get(id))

@app.route('/offers', methods=['POST', 'PUT'])
def add_offer():
    data = request.json
    offer = Offer(
        order_id=data.get('order_id'),
        executor_id=data.get('executor_id')
    )
    session.add(offer)
    session.commit()
    return jsonify(offer)

@app.route('/offers/<int:id>', methods=['DELETE'])
def delete_offer_by_id(id):
    offer = session.query(Offer).get(id)
    session.delete(offer)
    session.commit()
    return jsonify('')

if __name__ == "__main__":
    app.run()