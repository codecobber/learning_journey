from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Map the root URL ("/") to this function
@app.route("/")
def home_screen():
    return "<h1>01_Basics: Hello from the root path!</h1>"

# Start the live development server on port 5001
if __name__ == "__main__":
    app.run(debug=True, port=5001)
