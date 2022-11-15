from flask import Blueprint, request, jsonify
from models.ContactModel import Contact
from database.db import db
from logging import exception


contacts = Blueprint('contacts', __name__)

# ================== Routes ==================#
# ---------- "/"  | [Get] - all ---------- #
@contacts.route('/')
def home():
    try:
        contacts = Contact.query.all()

        # Uso de un generador
        toReturn = [contact.to_JSON() for contact in contacts]
        
        return jsonify(toReturn), 200
    except Exception:
        print('SERVER ERROR')
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Something went wrong"}), 500

# ---------- "/"  | [Get] - One ---------- #
@contacts.route('/<id>')
def get_contact(id):
    try:
        contact = Contact.query.get(id)

        # Uso de un generador
        toReturn = contact.to_JSON() 
        
        return jsonify(toReturn), 200
    except Exception:
        print('SERVER ERROR')
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Something went wrong"}), 500

# ---------- "/new" | [Post] ---------- #
@contacts.route('/new', methods=['POST'])
def add_contact():
    try:
        username = request.json['username']
        email = request.json['email']
        phone = request.json['phone']

        new_contact = Contact(username, email, phone)

        db.session.add(new_contact)
        db.session.commit()

        return f"{username}, {email}, {phone}"

    except Exception:
        print('SERVER ERROR')
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Something went wrong"}), 500

# ---------- "/update" | [Update] ---------- #
@contacts.route('/update/<id>', methods=['PUT', 'GET'])
def update_contact(id):
    
    try:
        contact = Contact.query.get(id)

        if request.method == 'PUT':
            contact.username = request.json['username']
            contact.email = request.json['email']
            contact.phone = request.json['phone']

            db.session.commit()
            return jsonify({'msg': 'updating'}), 200

        toReturn = contact.to_JSON() 

        return jsonify(toReturn), 200
    except Exception:
        print('SERVER ERROR')
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Something went wrong"}), 500

# ---------- "/delete/<id>" | [Delete] ---------- #
@contacts.route('/delete/<id>', methods=['DELETE'])
def delete_contact(id):

    try:
        contact = Contact.query.get(id)
        db.session.delete(contact)
        db.session.commit()

        return jsonify({"msg": f"Success, contact id: {id} deleted"}), 200
    except:
        print('SERVER ERROR')
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Something went wrong"}), 500

# ---------- "/about" ---------- #
@contacts.route('/about')
def add_about():
    return 'about'