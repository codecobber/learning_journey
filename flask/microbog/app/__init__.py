from flask import Flask

# Create the application engine variable
app = Flask(__name__)

# Load the routes from our package folder
from app import routes
