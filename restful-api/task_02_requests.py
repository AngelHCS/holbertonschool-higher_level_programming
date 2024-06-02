#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from a JSON API and prints their titles.

    This function sends a GET request
    to retrieve posts in JSON format. It then prints the titles of the posts.

    Returns:
        None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """
    Fetches posts from a JSON API and saves them to a CSV file.

    This function sends a GET request
    to retrieve posts in JSON format. It then creates a list of dictionaries
    contains post details (id, title, body), and writes them to a CSV file.

    Returns:
        None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        posts_list = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_list)

        print("Posts have been saved to posts.csv")
    else:
        print("Failed to fetch posts")
