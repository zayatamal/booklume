import json
from pathlib import Path

title = input("Book Title:")
author = input("Author Name:")
rating = input("Give your star rating between 1 to 5: ")
review_text = input("Write your Review: ")
review = {
    "title": title,
    "author": author,
    "rating": rating,
    "review": review_text,
}
reviews_path = Path("reviews.json")
try:
    with open(reviews_path, "r") as f:
        reviews = json.load(f)
except:
    reviews = []

reviews.append(review)

with open("reviews.json", "w") as f:
    json.dump(reviews, f, indent=4)
print("✅ Review saved!")
