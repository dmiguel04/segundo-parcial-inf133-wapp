from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from models import User, Patient
from view import auth_bp, patient_bp

app.register_blueprint(auth_bp)
app.register_blueprint(patient_bp)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    if not os.path.exists('app.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
