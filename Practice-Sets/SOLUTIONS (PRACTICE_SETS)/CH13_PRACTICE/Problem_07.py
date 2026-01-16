"""
Explore the Flask Python web framework and develop a basic web server application.
The application should initialize a Flask server, define at least one HTTP route, and return
a response when accessed through a web browser.

The objective is to demonstrate an understanding of:

-> Flask application setup

-> Route definition

-> Running a local development web server
 """
# ============================================================
# Program: Basic Web Server using Flask
# Description:
# This program demonstrates how to create a simple and
# scalable web server using the Flask framework.
#
# HOW TO RUN:
#   1. Install Flask:
#        pip install flask
#   2. Run the application:
#        python Problem_07.py
#
# HOW TO CHECK (Open in a Web Browser):
#   http://127.0.0.1:5000/              -> Home Page
#   http://127.0.0.1:5000/about         -> About Page
#   http://127.0.0.1:5000/health        -> Health Check
#   http://127.0.0.1:5000/greet/Shivansh -> Dynamic Greeting
# ============================================================

from flask import Flask, jsonify

# ------------------------------------------------------------
# Create Flask application instance
# ------------------------------------------------------------
app = Flask(__name__)


# ------------------------------------------------------------
# Route: Home Page
# ------------------------------------------------------------
@app.route("/")
def home():
    return "Welcome to the Flask Web Server!"


# ------------------------------------------------------------
# Route: About Page
# ------------------------------------------------------------
@app.route("/about")
def about():
    return "This application is built using Flask and Python."


# ------------------------------------------------------------
# Route: Health Check
# ------------------------------------------------------------
@app.route("/health")
def health_check():
    return jsonify(
        status="UP",
        message="Server is running successfully"
    )


# ------------------------------------------------------------
# Route: Greet User (Dynamic URL)
# ------------------------------------------------------------
@app.route("/greet/<username>")
def greet_user(username):
    return f"Hello {username}, welcome to the Flask server!"


# ------------------------------------------------------------
# Application entry point
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
