# Import flask
from flask import Flask

# Import a module / component
from app.mod_auth.controllers import mod_auth as auth_module

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Register blueprints
app.register_blueprint(auth_module)
