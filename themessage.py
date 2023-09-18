from bs4 import BeautifulSoup
from urllib.request import urlopen

letter = "B"

url = f"https://churchages.net/en/sermons/branham/{letter}/"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

query = soup.find_all('div', class_='cards')[0].contents

N = len(query)

# find all sermons for alphabet letter
for j in range(3, N, 2):
    print('Name: '+query[j].text+ '\n' + 'Link: '+ query[j].get('href'))

print("-"*100)

# find and select a certain sermon

sermon_no = 2

paragraph_no = 3

# has to be an odd number for some reason
if sermon_no % 2 == 0:
    sermon_no = sermon_no + 1

sermon_no = sermon_no+2

for i in range(sermon_no, sermon_no+2, 2):
    print('Name: '+query[i].text+ '\n' + 'Link: '+ query[i].get('href'))
    text_url = query[i].get('href')

    text_page = urlopen(text_url)
    text_html = text_page.read().decode("utf-8")
    text_soup = BeautifulSoup(text_html, "html.parser")

    text_query = text_soup.find_all('article')[0].get_text().split(".net")
    meta_data = text_query[0]
    title = meta_data.split("Preached")[0]
    preaching_text = text_query[1].split("\n") #split by paragraph number
    K = len(preaching_text) # no of paragraphs

print(K)
print(preaching_text[paragraph_no-1]) # zero indexed list

# print(query)

