from flask import Flask, request, jsonify
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SECRET_KEY"] = "your_secret_key"

    @app.route("/")
    def home():
        return "Restaurant Complaint API - Live!"

    @app.route("/api/complaints", methods=["POST"])
    def create_complaint():
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        return jsonify({"message": "Complaint received", "data": data}), 201

    @app.route("/api/complaints", methods=["GET"])
    def get_complaints():
        mock_complaints = [
            {"id": 1, "message": "Food was cold"},
            {"id": 2, "message": "Service was slow"},
        ]
        return jsonify(mock_complaints), 200

    @app.route("/api/complaints/<int:complaint_id>", methods=["GET"])
    def get_complaint(complaint_id):
        mock_complaint = {"id": complaint_id, "message": "Mock complaint message"}
        return jsonify(mock_complaint), 200

    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "healthy"}), 200

    return app
