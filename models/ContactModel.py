from database.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70))
    email = db.Column(db.String(70))
    phone = db.Column(db.String(16))

    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone

    def to_JSON(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
        }