import csv
# 1. Add 'render_template' to your imports at the top
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to your Crypto Tracker Dashboard!</h1><p>Go to <a href='/token/ripple'>/token/ripple</a> to see the scraped data.</p>"

# --- THE DYNAMIC DATA ROUTE ---
@app.route("/token/<token_name>")
def show_crypto_data(token_name):
    token_name = token_name.lower()
    filename = f"{token_name}_tweets.csv"
    
    # Create an empty Python list to hold just our text headlines
    headlines_list = []
    
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None) # skip header
            
            for row in reader:
                # Instead of building raw HTML strings, we just append 
                # the raw text to our Python list!
                headlines_list.append(row[1])
                
        # 2. This is where the magic happens!
        # We pass the template name, and then hand over our Python variables
        return render_template("dashboard.html", token=token_name, headlines=headlines_list)

    except FileNotFoundError:
        return f"<h2>⚠️ Error: No data found for '{token_name}'. Make sure {filename} exists!</h2>", 404

if __name__ == "__main__":
    app.run(debug=True, port=5002)
