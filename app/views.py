from flask import jsonify
from app import app

@app.get("/healthcheck")
def healthcheck():
    """Simple healthcheck endpoint."""
    return jsonify(status="ok"), 200
