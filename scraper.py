import requests
from  bs4 import BeautifulSoup
link_of_page = 'https://en.wikipedia.org/wiki/Olive_oil'

def get_counter(link_of_page):
    page = requests.get(link_of_page)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_sup = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    counter = 0
    for post in all_sup:
        counter += 1
    print(f" {counter}  Number of Citations needed")
    return counter

get_counter(link_of_page)

def get_citations_needed_report(link_of_page):
    page = requests.get(link_of_page)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_div = soup.find('div', class_="mw-body-content mw-content-ltr")
    all_p = all_div.find_all("p")
    list = []
    for paragraph in all_p:
        citation = paragraph.find_all("sup", class_="noprint Inline-Template Template-Fact")
        if citation:
            list.append(paragraph.text)
    for p in list:
        print(f"\n {p} \n")

get_citations_needed_report(link_of_page)   