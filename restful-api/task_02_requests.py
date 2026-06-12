#!/usr/bin/python3
"""Module for consuming an API using requests and saving data to CSV."""

import csv
import requests


def fetch_and_print_posts():
    """Fetch posts from an API and print their titles."""
    # 1. Définir l'URL
    url = "https://jsonplaceholder.typicode.com/posts"

    # 2. Envoyer une requête GET
    response = requests.get(url)

    # 3. Afficher le status code
    print("Status Code:", response.status_code)

    # 4. Si la requête réussit, convertir en JSON
    if response.status_code == 200:
        posts = response.json()

        # 5. Parcourir les posts et afficher chaque title
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts from an API and save selected fields to a CSV file."""
    # 1. Définir l'URL
    url = "https://jsonplaceholder.typicode.com/posts"

    # 2. Envoyer une requête GET
    response = requests.get(url)

    # 3. Si la requête réussit, convertir en JSON
    if response.status_code == 200:
        posts = response.json()

    # 4. Créer une liste contenant seulement id, title, body
        selected_posts = []
        for post in posts:
            selected_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

    # 5. Écrire cette liste dans posts.csv avec csv.DictWriter
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in selected_posts:
                writer.writerow(post)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
