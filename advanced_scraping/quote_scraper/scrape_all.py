import csv  # 1. Import Python's built-in CSV toolimport requests
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
		
		# 5. Find ALL quote containers on the page (this returns a list)
		all_quote_divs = soup.find_all("div", class_="quote")
		
		print(f"\nFound {len(all_quote_divs)} quotes on this page!")
		print("--------------------------------------------------")
		
		# 6. Because all_quote_divs is an iterable list, we can loop through it!
		for quote_div in all_quote_divs:
			# Inside the loop, quote_div represents ONE single quote container
			quote_text = quote_div.find("span", class_="text").text
			author_name = quote_div.find("small", class_="author").text
			
			# Print each one beautifully
			print(f'"{quote_text}"')
			print(f"By: {author_name}")
			print("-" * 30) # Prints a divider line between quotes
			
		
		
		# Print the clean results to the screen
		print("\n--- First Quote Found ---")
		print(f'"{quote_text}"')
		print(f"By: {author_name}\n")

	else:
		print(f"Failed to fetch the page. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
