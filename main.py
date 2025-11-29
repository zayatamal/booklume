import json

title = input("Book Title:")
author = input("Author Name:")
rating = input("Give your star rating between 1 to 5 ")
review_text = input("Write your Review")
review = {"title": title, "author": author, "rating": rating, "review": review_text}
