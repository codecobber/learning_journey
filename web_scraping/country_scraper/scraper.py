import requests

# Constants use UPPER_SNAKE_CASE
API_URL = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"


def fetch_countries():
    """Fetches and displays a list of countries from a public API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Variable names use standard snake_case. Notice the list comprehension!
        country_names = [country["name"]["common"] for country in data]
        
        print(f"List size of countries: {len(country_names)}")

        print("Successfully fetched country data:")
        for name in sorted(country_names)[:10]:
            print(f"- {name}")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    fetch_countries()
