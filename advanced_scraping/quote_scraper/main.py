import requests
from bs4 import BeautifulSoup

def main():

	# 1. Define the URL we want to target
	URL = "https://quotes.toscrape.com/"

	# 2. Grab the raw page data using requests
	print("Connecting to the website...")
	response = requests.get(URL)

	# 3. Check if the connection was successful (Status 200)
	if response.status_code == 200:
		print("Success! Page fetched.")
		
		# 4. Feed the raw HTML text into BeautifulSoup
		soup = BeautifulSoup(response.text, "html.parser")
		
		# 5. Find the very first quote container on the page
		# In the website's code, each quote lives inside a <div class="quote">
		first_quote_div = soup.find("div", class_="quote")
		
		# 6. Extract the text of the quote itself (stored inside a <span class="text">)
		quote_text = first_quote_div.find("span", class_="text").text
		
		# 7. Extract the author (stored inside a <small class="author">)
		author_name = first_quote_div.find("small", class_="author").text
		
		# Print the clean results to the screen
		print("\n--- First Quote Found ---")
		print(f'"{quote_text}"')
		print(f"By: {author_name}\n")

	else:
		print(f"Failed to fetch the page. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
