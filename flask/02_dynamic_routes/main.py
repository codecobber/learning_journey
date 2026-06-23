#project 02_dynamic_routes

from flask import Flask

app = Flask(__name__) #makes a flask object

@app.route("/")
def home():
    return "<h1>02_Dynamic Routes: Try adding '/user/ripple' to the URL above!</h1>"

# --- THE WILD CARD ---
# Flask captures whatever is typed after /user/ and drops it into the variable
@app.route("/user/<username>")
def show_user_profile(username):
    return f"<h2>Viewing real-time data for tracking token: @{username}</h2>"

if __name__ == "__main__":
    app.run(debug=True, port=5002) # Running this task on 5002!
