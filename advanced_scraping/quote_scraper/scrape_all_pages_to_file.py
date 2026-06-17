import csv
import requests
from bs4 import BeautifulSoup


def main():
    # 1. Define the base website address
    BASE_URL = "https://quotes.toscrape.com"

    # 2. Start at the very first page relative path
    current_page_path = "/page/1/"

    print("Opening quotes.csv to start recording data...")

    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])

        # 3. This loop will keep running as long as current_page_path has a value
        while current_page_path:
            # Construct the full URL (e.g., https://quotes.toscrape.com/page/1/)
            full_url = BASE_URL + current_page_path
            print(f"Scraping: {full_url}")

            response = requests.get(full_url)

            if response.status_code != 200:
                print(
                    f"Stopped. Hit an error or block. Status: {response.status_code}"
                )
                break

            soup = BeautifulSoup(response.text, "html.parser")
            all_quote_divs = soup.find_all("div", class_="quote")

            # 4. Loop through and write all quotes on the CURRENT page
            for quote_div in all_quote_divs:
                quote_text = quote_div.find("span", class_="text").text
                author_name = quote_div.find("small", class_="author").text

                tag_elements = quote_div.find_all("a", class_="tag")
                tags_list = [tag.text for tag in tag_elements]
                tags_string = ", ".join(tags_list)

                writer.writerow([quote_text, author_name, tags_string])

            # 5. PAGINATION LOGIC: Look for the "Next" button
            # In this site's HTML, the next button lives inside a <li class="next">
            next_button_li = soup.find("li", class_="next")

            if next_button_li:
                # If found, extract the relative URL from its internal <a> tag
                # next_button_li.find('a')['href'] looks inside <a href="/page/2/"> and grabs "/page/2/"
                current_page_path = next_button_li.find("a")["href"]
            else:
                # If there is no next button, set path to None to break the while loop
                print("Reached the final page!")
                current_page_path = None

    print("\nSuccess! All pages crawled. Check your quotes.csv file.")


if __name__ == "__main__":
    main()
