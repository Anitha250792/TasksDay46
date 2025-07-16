from flask import Flask, request

app = Flask(__name__)

# Task 41: Define a route /hello that returns a welcome message.
@app.route('/hello')
def hello():
    return "Welcome to the /hello route! 🎉"

# Task 42: Add a route /user/<username> and return a dynamic message with the username.
@app.route('/user/<username>')
def show_user(username):
    return f"Hello, {username}! This is your personalized page."

# Task 43: Add multiple routes pointing to the same function.
@app.route('/about')
@app.route('/info')
def about():
    return "This is the about/info page. Both routes call the same function."

# Task 44: Add different HTTP methods (GET, POST) in a route and print the method used.
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "You used POST method to submit!"
    else:
        return "You used GET method to access this page."

# Task 45: Explain what happens when you define two functions with the same route.
# In Flask, defining two functions with the same route will cause an error,
# because only one function can be bound to a route at a time.
# Example (this code is commented to avoid breaking the app):

"""
@app.route('/duplicate')
def func1():
    return "This is function 1."

@app.route('/duplicate')
def func2():
    return "This is function 2."  # This will override func1 and cause an error in some cases.
"""

@app.route('/duplicate')
def func_correct():
    return "This function is correctly defined once for the route /duplicate."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
