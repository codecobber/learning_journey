import csv  # 1. Import Python's built-in CSV tool
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
		
		# 5. Find ALL quote containers on the page (this returns a list)
		all_quote_divs = soup.find_all("div", class_="quote")
		
		print(f"\nFound {len(all_quote_divs)} quotes on this page!")
		print("--------------------------------------------------")
		
		with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
			
			writer = csv.writer(file)
			
			# 3. Write the very first row containing our column headers
			writer.writerow(["Quote", "Author", "Tags"])
			
			# 6. Because all_quote_divs is an iterable list, we can loop through it!
			for quote_div in all_quote_divs:
				# Inside the loop, quote_div represents ONE single quote container
				quote_text = quote_div.find("span", class_="text").text
				author_name = quote_div.find("small", class_="author").text
				
				tag_elements = quote_div.find_all("a", class_="tag")
				tags_list = [tag.text for tag in tag_elements]
				tags_string = ", ".join(tags_list)
				
				# 5. Instead of just printing, we pack the strings into a list row
				# The CSV writer automatically handles quotes and commas safely!
				writer.writerow([quote_text, author_name, tags_string])
			
			print("Finished! Your file 'quotes.csv' is ready.")
			

	else:
		print(f"Failed to fetch the page. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
