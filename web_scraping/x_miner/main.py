import urllib.parse
from search_google import scrape_ripple_tweets as srt

def main():
	print("Hello from x-miner!")
	query = "site:x.com crypto"
	safe_query = urllib.parse.quote(query)

	print(safe_query) 
	# Output: site%3Ax.com%20crypto (Safe for Google's URL structure!)

	raw_url = "https://www.hedera.com/blog/index.html?author=admin"

	# Parse the URL string into an object structure
	parsed_data = urllib.parse.urlparse(raw_url)

	print(f"Protocol: {parsed_data.scheme}")   # Output: https
	print(f"Domain:   {parsed_data.netloc}")   # Output: www.hedera.com
	print(f"Path:     {parsed_data.path}")     # Output: /blog/index.html
	print(f"Query:    {parsed_data.query}")    # Output: author=admin
	
	srt() #call scrape_ripple_tweets function


if __name__ == "__main__":
    main()
    


