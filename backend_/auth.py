from flask import jsonify
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

from database import SessionLocal

def login_user(data):
    session = SessionLocal()  # Create session
    try:
        email = data.get("email")
        password = data.get("password")

        user = session.query(User).filter_by(user_email=email).first()

        if user and check_password_hash(user.hashed_password, password):
            return jsonify({"message": "Login successful", "user": email}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Debugging: return error message
    finally:
        session.close()  # Always close session


def register_user(data):
    session = SessionLocal()

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone = data.get("phone")
    user_email = data.get("email")
    password = data.get("hashed_password")

    # Debugging: Print to check if password is received
    print(first_name)
    print("Received password:", password)
    if not password:
        return jsonify({"error": "Password is required"}), 400

    hashed_password = generate_password_hash(password)  # Hash password

    new_user = User(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        user_email=user_email,
        hashed_password=hashed_password
    )

    session.add(new_user)
    session.commit()
    return jsonify({"message": "User registered successfully"}), 201
