from flask import Flask

app = Flask(__name__)

# Task 46: Return a basic HTML structure
@app.route('/basic')
def basic_html():
    return "<html><body><h1>Welcome to Flask!</h1><p>This is a basic HTML response.</p></body></html>"

# Task 47: Add inline CSS styling to the returned HTML
@app.route('/styled')
def styled_html():
    return '''
    <html>
        <body>
            <h1 style="color: blue; text-align: center;">Flask with Inline CSS</h1>
            <p style="font-size: 18px; color: green;">This paragraph has custom styling using inline CSS.</p>
        </body>
    </html>
    '''

# Task 48: Return a multiline HTML string using triple-quoted string
@app.route('/multiline')
def multiline_html():
    return """
    <html>
        <body>
            <h1>Multiline HTML Example</h1>
            <p>This HTML content is written using a Python triple-quoted string.</p>
            <p>You can easily write multiple lines and include line breaks for readability.</p>
        </body>
    </html>
    """

# Task 49: Return an unordered list with 3 items
@app.route('/list')
def unordered_list():
    return """
    <html>
        <body>
            <h1>My Favorite Fruits</h1>
            <ul>
                <li>Apple</li>
                <li>Banana</li>
                <li>Cherry</li>
            </ul>
        </body>
    </html>
    """

# Task 50: Use basic HTML tags and explain
@app.route('/tags')
def basic_tags():
    return """
    <html>
        <body>
            <h1>HTML Tags Example</h1>
            <p>This is a paragraph tag. It groups text into paragraphs.</p>
            <p>Here's another paragraph.<br>Notice the line break tag (&lt;br&gt;) above.</p>
            <hr>
            <p>The horizontal rule tag (&lt;hr&gt;) above draws a line to separate sections.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
