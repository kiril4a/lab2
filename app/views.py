from flask import jsonify, request
from app import app
from app.models import (
    create_user, get_user, delete_user, get_all_users,
    create_category, get_all_categories, delete_category,
    create_record, get_record, delete_record, get_records
)


@app.get("/healthcheck")
def healthcheck():
    """Simple healthcheck endpoint."""
    return jsonify(status="ok"), 200


# ================== USER ENDPOINTS ==================

@app.route("/user", methods=["POST"])
def create_user_endpoint():
    """Create a new user"""
    data = request.get_json()
    
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    
    user = create_user(data["name"])
    return jsonify(user.to_dict()), 201


@app.route("/user/<int:user_id>", methods=["GET"])
def get_user_endpoint(user_id):
    """Get user by ID"""
    user = get_user(user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user.to_dict()), 200


@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user_endpoint(user_id):
    """Delete user by ID"""
    if delete_user(user_id):
        return jsonify({"message": "User deleted successfully"}), 200
    
    return jsonify({"error": "User not found"}), 404


@app.route("/users", methods=["GET"])
def get_users_endpoint():
    """Get all users"""
    users = get_all_users()
    return jsonify([user.to_dict() for user in users]), 200


# ================== CATEGORY ENDPOINTS ==================

@app.route("/category", methods=["POST"])
def create_category_endpoint():
    """Create a new category"""
    data = request.get_json()
    
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    
    category = create_category(data["name"])
    return jsonify(category.to_dict()), 201


@app.route("/category", methods=["GET"])
def get_categories_endpoint():
    """Get all categories"""
    categories = get_all_categories()
    return jsonify([category.to_dict() for category in categories]), 200


@app.route("/category", methods=["DELETE"])
def delete_category_endpoint():
    """Delete category by ID"""
    data = request.get_json()
    
    if not data or "id" not in data:
        return jsonify({"error": "Category ID is required"}), 400
    
    category_id = data["id"]
    
    if delete_category(category_id):
        return jsonify({"message": "Category deleted successfully"}), 200
    
    return jsonify({"error": "Category not found"}), 404


# ================== RECORD ENDPOINTS ==================

@app.route("/record", methods=["POST"])
def create_record_endpoint():
    """Create a new expense record"""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    
    required_fields = ["user_id", "category_id", "amount"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400
    
    try:
        user_id = int(data["user_id"])
        category_id = int(data["category_id"])
        amount = float(data["amount"])
    except ValueError:
        return jsonify({"error": "Invalid data types"}), 400
    
    record = create_record(user_id, category_id, amount)
    
    if not record:
        return jsonify({"error": "User or category not found"}), 404
    
    return jsonify(record.to_dict()), 201


@app.route("/record/<int:record_id>", methods=["GET"])
def get_record_endpoint(record_id):
    """Get record by ID"""
    record = get_record(record_id)
    
    if not record:
        return jsonify({"error": "Record not found"}), 404
    
    return jsonify(record.to_dict()), 200


@app.route("/record/<int:record_id>", methods=["DELETE"])
def delete_record_endpoint(record_id):
    """Delete record by ID"""
    if delete_record(record_id):
        return jsonify({"message": "Record deleted successfully"}), 200
    
    return jsonify({"error": "Record not found"}), 404


@app.route("/record", methods=["GET"])
def get_records_endpoint():
    """Get records filtered by user_id and/or category_id"""
    user_id = request.args.get("user_id", type=int)
    category_id = request.args.get("category_id", type=int)
    
    # Both parameters are optional, but at least one is required
    if user_id is None and category_id is None:
        return jsonify({"error": "At least one parameter (user_id or category_id) is required"}), 400
    
    records = get_records(user_id, category_id)
    return jsonify([record.to_dict() for record in records]), 200
