import csv
from flask import Flask

app = Flask(__name__) #make a flask object

@app.route("/")
def home():
    return "<h1>Welcome to your Crypto Tracker Dashboard!</h1><p>Go to <a href='/ripple'>/ripple</a> to see the scraped data.</p>"

# --- THE DATA ROUTE ---
@app.route("/ripple")
def show_ripple_data():
    # 1. Create an empty HTML string to build our list
    html_output = "<h1>Live Ripple Scraped Headlines</h1><ul>"
    
    # 2. Open your existing CSV file (make sure the filename matches yours!)
    with open("ripple_tweets.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        
        # Skip the header row if your CSV has one (e.g., ["Timestamp", "Tweet"])
        next(reader, None) 
        
        # 3. Loop through every row in the CSV file
        for row in reader:
            # Assuming row is where the actual tweet text sits
            tweet_text = row 
            # Wrap the tweet text in HTML list item tags <li>
            html_output += f"<li>{tweet_text}</li>"
            
    # 4. Close the HTML list tag
    html_output += "</ul>"
    
    # 5. Send the finished HTML string back to the browser!
    return html_output
    
# --- THE DYNAMIC DATA ROUTE ---
@app.route("/token/<token_name>")
def show_crypto_data(token_name):
    # Lowercase the input just to be safe with filenames
    token_name = token_name.lower()
    filename = f"{token_name}_tweets.csv"
    
    html_output = f"<h1>Live {token_name.upper()} Scraped Headlines</h1><ul>"
    
    try:
        # Flask tries to open the file based on whatever was typed in the URL!
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None) # skip header
            
            for row in reader:
                html_output += f"<li>{row}</li>"
                
        html_output += "</ul>"
        return html_output

    except FileNotFoundError:
        # A clean error message if they search for a token you haven't scraped yet
        return f"<h2>⚠️ Error: No data found for '{token_name}'. Make sure {filename} exists!</h2>", 404

if __name__ == "__main__":
    app.run(debug=True, port=5002)
