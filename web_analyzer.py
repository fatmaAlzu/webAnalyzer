import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    
    num_headings = sum(len(soup.find_all(f"h{i}")) for i in range(1, 7))
    num_links = len(soup.find_all("a"))
    num_paragraphs = len(soup.find_all("p"))

    print(f"Number of headings: {num_headings}")
    print(f"Number of links: {num_links}")
    print(f"Number of paragraphs: {num_paragraphs}")

    webpage_text = soup.get_text().lower()
    keyword = input("\nEnter a keyword to search for: ").strip().lower()
    keyword_count = webpage_text.count(keyword)
    print(f"Number of occurrences of '{keyword}': {keyword_count}")


except Exception as e:
    print(f"Error fetching content: {e}")

print(soup.prettify())