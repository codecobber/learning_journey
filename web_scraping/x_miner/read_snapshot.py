import csv

print("--- 🗞️ Ripple X.com Snapshot Headlines ---")

# Open the snapshot file safely using Python's built-in file handler
with open("ripple_tweets.csv", mode="r", encoding="utf-8") as file:
    # Use the CSV reader module to split rows automatically
    reader = csv.reader(file)

    # Skip the header row (Tweet URL, Tweet Summary Snippet)
    next(reader)

    # Loop through each row and print just the headline
    count = 1
    for row in reader:
        # row[0] is the URL, row[1] is the text snippet (the headline!)
        headline = row[1]

        print(f"{count}. {headline}")
        print("-" * 40)  # Visual divider
        count += 1
