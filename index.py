from app import app

from database.db import db

#Cuando arranque la aplicacion creará las tablas dee contact.py


db.init_app(app)
with app.app_context(): 
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)