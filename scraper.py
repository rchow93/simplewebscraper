#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import os
import urllib
import hashlib
import sys
import argparse
import time

# Default URL
default_url = "https://docs.llamaindex.ai/en/stable/examples/"

# Set up argument parser
parser = argparse.ArgumentParser(description='Scrape a website.')
parser.add_argument('url', nargs='?', default=default_url, help='The URL to scrape')
parser.add_argument('-t', '--time', type=int, default=2, help='Time to wait before scraping the next page (in seconds)')
args = parser.parse_args()

# Use the parsed URL and time
url = args.url
wait_time = args.time

# The directory to store files in
output_dir = "./data/"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def safe_filename(url, max_length=255):
    """Generate a safe filename by truncating or hashing if necessary."""
    file_name = os.path.basename(url.rstrip('/')) or 'index.html'
    if len(file_name) > max_length:
        # Use a hash to ensure uniqueness if the filename is too long
        file_name = hashlib.md5(file_name.encode('utf-8')).hexdigest() + '.html'
    return file_name

def scrape_page(url, visited, depth, max_depth):
    if url in visited or depth > max_depth:
        return
    visited.add(url)

    try:
        # Fetch the page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Generate a valid file name
        file_name = safe_filename(url)
        file_path = os.path.join(output_dir, file_name)

        # Print the name of the HTML page being scraped
        print(f"Scraping and saving: {file_name}")

        # Write the page to a file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)

        # Find all links
        links = soup.find_all("a", href=True)
        for link in links:
            href = link["href"]
            # Check if the link is a relative URL and resolve it
            if not href.startswith("http"):
                href = urllib.parse.urljoin(url, href)
            # Ensure the link is within the same domain
            if href.startswith(url):
                time.sleep(wait_time)  # Wait before scraping the next page
                scrape_page(href, visited, depth + 1, max_depth)
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Start scraping from the main URL with a maximum depth of 3
scrape_page(url, set(), 0, 3)
