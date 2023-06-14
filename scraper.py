import requests
from  bs4 import BeautifulSoup
import json

URL = 'https://en.wikipedia.org/wiki/Washington,_D.C.'
def  get_citations_needed_count (URL):
    page = requests.get(URL)
    # print(page.content)
    soup = BeautifulSoup(page.content,'html.parser')
    # print(soup)
    all_posts = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    # print(all_posts)
    citations_needed_count = 0
    for post in all_posts:
        citations_needed_count += 1
    return citations_needed_count
print("Number Of citations needed is ",get_citations_needed_count(URL))