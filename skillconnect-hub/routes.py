from flask import Blueprint, jsonify

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return jsonify({"message": "Welcome to SkillConnect Hub API!"})

