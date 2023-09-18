from bs4 import BeautifulSoup
from urllib.request import urlopen

letter = "A"

url = f"https://churchages.net/en/sermons/branham/{letter}/"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

query = soup.find_all('div', class_='cards')[0].contents

N = len(query) # number of sermons starting with the input letter

# find and collect all sermons for alphabet letter
sermons_list = []
for j in range(3, N, 2):
    # print('Name: '+query[j].text+ '\n' + 'Link: '+ query[j].get('href'))
    sermonObj = {'title':query[j].text[0:-10], 'date':query[j].text[-10:], 'link': query[j].get('href')}
    sermons_list.append(sermonObj)
    print(sermonObj)

print("-"*100)

s = 1 # sermon index

print(len(sermons_list), '\n')
print(sermons_list, '\n')
print(sermons_list[s-1], '\n')

print("-"*100)

# find and select a certain sermon

sermon_no = 2

paragraph_no = 12

# has to be an odd number for some reason
if sermon_no % 2 == 0:
    sermon_no = sermon_no + 1

sermon_no = sermon_no+2 # for some reason, I have to start from 3

# parse sermon
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

K = len(preaching_text) -1 # no of paragraphs because of zero indexing

print('Paragraph: ', paragraph_no, ' out of', K)
print(preaching_text[paragraph_no-1]) # zero indexed list

