# app.py

# Task 22: Import Flask correctly
from flask import Flask

# Task 23: Create a basic Flask application instance
app = Flask(__name__)

# Task 24: Add a basic home route / that returns "Hello, Flask!"
@app.route('/')
def home():
    return "Hello, Flask!"

# Task 26: Add another route /about returning "This is the about page"
@app.route('/about')
def about():
    return "This is the about page"

# Task 27: Print something in the console when the server starts
print("Flask server is starting...")

# Task 29: Create an app.run(debug=True) statement and explain the debug mode
# Debug mode allows automatic reloading on code changes and shows detailed error pages.
if __name__ == '__main__':
    app.run(debug=True)

# Task 28: Comments are already added above explaining each section
