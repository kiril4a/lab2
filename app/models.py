from datetime import datetime
from typing import Optional

# In-memory storage (for simplicity)
users = {}
categories = {}
records = {}

# ID counters
user_id_counter = 1
category_id_counter = 1
record_id_counter = 1


class User:
    """User model"""
    def __init__(self, name: str):
        global user_id_counter
        self.id = user_id_counter
        user_id_counter += 1
        self.name = name
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Category:
    """Category model"""
    def __init__(self, name: str):
        global category_id_counter
        self.id = category_id_counter
        category_id_counter += 1
        self.name = name
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Record:
    """Expense record model"""
    def __init__(self, user_id: int, category_id: int, amount: float):
        global record_id_counter
        self.id = record_id_counter
        record_id_counter += 1
        self.user_id = user_id
        self.category_id = category_id
        self.created_at = datetime.now().isoformat()
        self.amount = amount
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "category_id": self.category_id,
            "created_at": self.created_at,
            "amount": self.amount
        }


# Storage functions
def create_user(name: str) -> User:
    """Create a new user"""
    user = User(name)
    users[user.id] = user
    return user


def get_user(user_id: int) -> Optional[User]:
    """Get user by ID"""
    return users.get(user_id)


def delete_user(user_id: int) -> bool:
    """Delete user by ID"""
    if user_id in users:
        del users[user_id]
        return True
    return False


def get_all_users():
    """Get all users"""
    return list(users.values())


def create_category(name: str) -> Category:
    """Create a new category"""
    category = Category(name)
    categories[category.id] = category
    return category


def get_all_categories():
    """Get all categories"""
    return list(categories.values())


def delete_category(category_id: int) -> bool:
    """Delete category by ID"""
    if category_id in categories:
        del categories[category_id]
        return True
    return False


def create_record(user_id: int, category_id: int, amount: float) -> Optional[Record]:
    """Create a new expense record"""
    # Validate that user and category exist
    if user_id not in users:
        return None
    if category_id not in categories:
        return None
    
    record = Record(user_id, category_id, amount)
    records[record.id] = record
    return record


def get_record(record_id: int) -> Optional[Record]:
    """Get record by ID"""
    return records.get(record_id)


def delete_record(record_id: int) -> bool:
    """Delete record by ID"""
    if record_id in records:
        del records[record_id]
        return True
    return False


def get_records(user_id: Optional[int] = None, category_id: Optional[int] = None):
    """Get records filtered by user_id and/or category_id"""
    result = list(records.values())
    
    if user_id is not None:
        result = [r for r in result if r.user_id == user_id]
    
    if category_id is not None:
        result = [r for r in result if r.category_id == category_id]
    
    return result
