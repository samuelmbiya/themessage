from bs4 import BeautifulSoup
from urllib.request import urlopen

letter = "B"

url = f"https://churchages.net/en/sermons/branham/{letter}/"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

query = soup.find_all('div', class_='cards')[0].contents

N = len(query)

for i in range(3, 5, 2):
    print('Name: '+query[i].text+ '\n' + 'Link: '+ query[i].get('href'))
    text_url = query[i].get('href')

    text_page = urlopen(text_url)
    text_html = text_page.read().decode("utf-8")
    text_soup = BeautifulSoup(text_html, "html.parser")

    text_query = text_soup.find_all('article')[0].get_text().split(".net")
    meta_data = text_query[0]
    title = meta_data.split("Preached")[0]
    preaching_text = text_query[1].split("\n") #split by paragraph number
    K = len(preaching_text)
    k = 6 #zero indexed list
    # print(K)
    print(preaching_text[k])

