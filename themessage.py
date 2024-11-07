from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import etree

letter = "G"

url = f"https://churchages.net/en/sermons/branham/{letter}/"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# for xref in soup("xref"):
#     xref.decompose()


query = soup.find_all('div', class_='cards')[0].contents

N = len(query) # number of sermons starting with the input letter

# find and collect all sermons for alphabet letter
sermons_list = []
for j in range(3, N, 2):
    # print('Name: '+query[j].text+ '\n' + 'Link: '+ query[j].get('href'))
    sermonObj = {'title':query[j].text[0:query[j].text.find("1")], 'date':query[j].text[query[j].text.find("1"):len(query[j].text)], 'link': query[j].get('href')}
    print(j//2, sermonObj)
    sermons_list.append(sermonObj)

# print(sermons_list)

print("-"*100)

s = 91 # sermon index
p = 1 # paragraph

# print(len(sermons_list), '\n')
# print(sermons_list, '\n')
# print(sermons_list[s-1], '\n')

# print("-"*100)

# find and select a certain sermon

sermon_no = s

paragraph_no = p

# has to be an odd number for some reason
if sermon_no % 2 == 0:
    sermon_no = sermon_no + 1

sermon_no = sermon_no+2 # for some reason, I have to start from 3

# parse sermon

sermonObj = sermons_list[s-1]

text_page = urlopen(sermonObj['link'])
text_html = text_page.read().decode("utf-8")
text_soup = BeautifulSoup(text_html, "html.parser")

# print(text_soup)
xref_all = text_soup.find_all(attrs={"class": "Xrefs"})
[xref.decompose() for xref in xref_all]

text_query = text_soup.find_all('article')[0].get_text().split(".net")
meta_data = text_query[0]
title = meta_data.split("Preached")[0]
preaching_text = text_query[1].split("\n") #split by paragraph number

K = len(preaching_text) -1 # no of paragraphs because of zero indexing

print('Title: ', sermonObj['title'])
print('Date: ', sermonObj['date'])
print('Paragraph: ', paragraph_no, ' out of', K)

# print(preaching_text[paragraph_no-1]) # zero indexed list

# for p_no in range(1,K+1,1):
#     print(preaching_text[p_no-1] + "\n") # zero indexed list

song_string = '\n'
verse_order = ''
for p_no in range(1,K+1,1):
    # print(f'<verse label="{p_no}" type="custom">'+ f'<![CDATA[{preaching_text[p_no-1]}]]>'+ '</verse>')
    verse_order += f'v{p_no} '
    print(len(preaching_text[p_no-1].split("."))-1)
    # print(preaching_text[p_no-1].split("."))
    song_string += f'    <verse name="v{p_no}">'+'\n'+f'      <lines>{preaching_text[p_no-1]}</lines>'+'\n'+'    </verse>'+'\n'
# print('<?xml version="1.0" encoding="utf-8"?>'+'\n'+'<song version="1.0" xmlns="http://openlyrics.info/namespace/2009/song">'+'<lyrics language="en">'+song_string+'<lyrics>'+'\n'+'</song>')

t = sermonObj['title']
d = sermonObj['date']
temp = d.split("-")
yy = temp[0][2:4]
mm = temp[1]
dd = temp[2]
t += f'{yy}-'+f'{mm}'+f'{dd}'

f = open(f'{t}'+'.xml', "w")
meta_data = '  <properties>'+'\n'+'    <titles>'+'\n'+f'      <title>{t}</title>'+'\n'+'    </titles>'+'\n'+f'    <verseOrder>{verse_order}</verseOrder>'+'\n'+'    <authors>'+'\n'+'      <author>VGR</author>'+'\n'+'    </authors>'+'\n'+'  </properties>'
f.write('<?xml version="1.0" encoding="utf-8"?>'+'\n'+'<song xmlns="http://openlyrics.info/namespace/2009/song" version="0.8" createdIn="OpenLP 3.0.2" modifiedIn="OpenLP 3.0.2" modifiedDate="2024-11-07T19:39:02">'+'\n'+meta_data+'\n'+'  <lyrics language="en">'+song_string+'  </lyrics>'+'\n'+'</song>')
f.close()

parser = etree.XMLParser(remove_blank_text=True)
parsed_file = etree.parse(open('Palmerworm, locust, cankerworm and caterpillar1953-06-12.xml', 'rb'), parser)
xml = etree.tostring(parsed_file).decode()
# print(xml)