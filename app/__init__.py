from flask import Flask

app = Flask(__name__)

from app import views

def create_app():
    """Return the existing Flask application instance for CLI compatibility."""
    return app