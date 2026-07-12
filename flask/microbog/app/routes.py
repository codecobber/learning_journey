
from flask import render_template
from app import app



# Your main home feed
posts_feed = [
    {'author': 'Alice', 'body': 'Beautiful day in Edinburgh today!'},
    {'author': 'Bob', 'body': 'The Geany editor is working perfectly.'},
    {'author': 'Charlie', 'body': 'Flask templates make sense now.'}
]

# Your new custom feed for trending posts
trending_feed = [
    {'author': 'Alice', 'body': 'Flask is taking over the world!'},
    {'author': 'Dave', 'body': 'Just learned about template inheritance, mind blown.'}
]

# Your new custom feed for bookmarked posts
bookmarked_feed = [
    {'author': 'Charlie', 'body': 'Cool Python trick of the day...'}
]
    
@app.route('/')

@app.route('/index')
def index():
    user_data = {'username': 'ThinkPad Developer'}
    
    # Hand off the template name and variables to Jinja
    return render_template('index.html', title='Home', user=user_data, posts=posts_feed)

@app.route('/about')
def about():
    # We pass a different title, but we don't need to pass posts or user data here
    return render_template('about.html', title='About Us')
# Inside routes.py

@app.route('/explore')
def explore():
    # Python sends the title "Trending Content" to index.html
    return render_template('explore.html', title='Trending Content', posts=trending_feed)

@app.route('/bookmarks')
def bookmarks():
    # Python sends the title "My Bookmarks" to the EXACT SAME index.html file
    return render_template('bookmarks.html', title='My Bookmarks', posts=bookmarked_feed)
