from flask import Flask, request, jsonify
from .extensions import cors


def create_app():
    app = Flask(__name__)

    # application configuration
    app.config["SECRET_KEY"] = "your_secret_key"

    # initialize extensions
    cors.init_app(app)

    # routes
    @app.route("/")
    def home():
        return "Restaurant Complaint API - Live!"

    @app.route("/api/complaints", methods=["POST"])
    def create_complaint():
        data = request.get_json()
        # Here you would typically save the complaint to a database
        # For now, we'll just return the data back as a response
        if not data:
            return jsonify({"error": "No data provided"}), 400
        return jsonify({"message": "Complaint received", "data": data}), 201

    @app.route("/api/complaints", methods=["GET"])
    def get_complaints():
        # Here you would typically fetch complaints from a database
        # For now, we'll return a mock list of complaints
        mock_complaints = [
            {"id": 1, "message": "Food was cold"},
            {"id": 2, "message": "Service was slow"},
        ]
        return jsonify(mock_complaints), 200

    @app.route("/api/complaints/<int:complaint_id>", methods=["GET"])
    def get_complaint(complaint_id):
        # Here you would typically fetch a specific complaint from a database
        # For now, we'll return a mock complaint
        mock_complaint = {"id": complaint_id, "message": "Mock complaint message"}
        return jsonify(mock_complaint), 200

    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "healthy"}), 200

    return app
