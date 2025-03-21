import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() 
    soup = BeautifulSoup(response.content, 'html.parser')
except Exception as e:
    print(f"Error fetching content: {e}")

num_headings = len(soup.find_all(re.compile('^h[1-6]$')))
num_links = len(soup.find_all("a"))
num_paragraphs = len(soup.find_all("p"))

print("\n--- Webpage Analysis ---")
print(f"Number of headings: {num_headings}")
print(f"Number of links: {num_links}")
print(f"Number of paragraphs: {num_paragraphs}")

webpage_text = soup.get_text().lower()  # Convert text to lowercase
keyword = input("\nEnter a keyword to search for: ").strip().lower()
keyword_count = webpage_text.count(keyword)

print(f"Number of occurrences of '{keyword}': {keyword_count}")

words = re.findall(r'\b\w+\b', webpage_text)  
word_counts = Counter(words) 
most_common_words = word_counts.most_common(5) 

print("\n--- Word Frequency Analysis ---")
for word, count in most_common_words:
    print(f"{word}: {count}")

paragraphs = soup.find_all('p')
longest_paragraph = ""
for p in paragraphs:
    text = p.get_text().strip()
    if len(text.split()) > len(longest_paragraph.split()) and len(text.split()) > 5:
        longest_paragraph = text
paragraph_word_count = len(longest_paragraph.split())

print("\n--- Longest Paragraph ---")
print(f"Longest paragraph ({paragraph_word_count} words): {longest_paragraph}")

labels = ['Headings', 'Links', 'Paragraphs']
values = [num_headings, num_links, num_paragraphs]

plt.bar(labels, values)
plt.title('Group 45')
plt.ylabel('Count')
plt.show()
