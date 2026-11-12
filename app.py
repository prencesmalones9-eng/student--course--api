from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = [
    {"id": 1, "code": "ITAS 3228", "name": "Web and Mobile Development", "description": "Build web & mobile apps"},
    {"id": 2, "code": "ITAS 3215", "name": "Database Management Systems", "description": "Design databases"},
    {"id": 3, "code": "ITAS 3203", "name": "System Analysis and Design", "description": "Design information systems"},
    {"id": 4, "code": "ITAS 3240", "name": "Computer Networks", "description": "Data communication & protocols"},
    {"id": 5, "code": "ITAS 3255", "name": "Information Security", "description": "Secure data & systems"}
]

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "API is running"})

@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = next((c for c in courses if c["id"] == course_id), None)
    if course:
        return jsonify(course)
    return jsonify({"error": "Course not found"}), 404

if _name_ == '_main_':
    app.run(host='0.0.0.0')