import csv
import time
import urllib.parse
import requests
from bs4 import BeautifulSoup


def scrape_ripple_tweets(max_pages=2):
    # 1. Define the advanced Google search query for Ripple on X/Twitter
    search_query = "site:x.com Ripple"

    # 2. Use quote() to find-and-replace spaces and colons with web-safe codes
    # "site:x.com Ripple" becomes "site%3Ax.com%20Ripple"
    encoded_query = urllib.parse.quote(search_query)

    # Fake a real browser header so Google processes our request normally
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # 3. Create/Open the CSV file to record our data
    with open(
        "ripple_tweets.csv", mode="w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["Tweet URL", "Tweet Summary Snippet"])  # CSV Headers

        page = 0
        while page < max_pages:
            # Google pagination tracks results by 10s (page 1 starts at 0, page 2 starts at 10)
            start_result = page * 10
            url = f"https://www.google.com/search?q={encoded_query}&start={start_result}"

            print(f"📡 Downloading page {page + 1} from Google Index...")
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                print(
                    f"⚠️ Google responded with status code {response.status_code}. Stopping script."
                )
                break

            # Parse the HTML text down into an organized node tree
            soup = BeautifulSoup(response.text, "html.parser")

            # Google wraps main web search entries in 'div' tags with a class of 'g'
            search_blocks = soup.select("div.g")

            if not search_blocks:
                print("ℹ️ No more search blocks found on this page.")
                break

            for block in search_blocks:
                # Isolate the anchor tag for the URL and the div tag containing the snippet text
                link_element = block.select_one("a")
                snippet_element = block.select_one("div.VwiC3b")

                if link_element and snippet_element:
                    tweet_url = link_element["href"]
                    tweet_text = snippet_element.get_text(strip=True)

                    # Ensure the link targets an individual status update (tweet)
                    if "status" in tweet_url:
                        writer.writerow([tweet_url, tweet_text])
                        print(f"✅ Logged Tweet: {tweet_url[:45]}...")

            # Increment page counter and implement an automated delay to mimic human behavior
            page += 1
            print("⏳ Pausing briefly to rest the connection...")
            time.sleep(3)

    print("\n🎉 Done! Run 'cat ripple_tweets.csv' to view your saved data.")


scrape_ripple_tweets(max_pages=2)
