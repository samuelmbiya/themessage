from bs4 import BeautifulSoup
from urllib.request import urlopen

letter = "P"

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

s = 2 # sermon index
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

song_string = ''
for p_no in range(1,K+1,1):
    # print(f'<verse label="{p_no}" type="custom">'+ f'<![CDATA[{preaching_text[p_no-1]}]]>'+ '</verse>')
    song_string += f'<verse label="{p_no}" type="custom">'+ f'<![CDATA[{preaching_text[p_no-1]}]]>'+ '</verse>'
print('<?xml version="1.0" encoding="utf-8"?>'+'<song version="1.0">'+'<lyrics language="en">'+song_string+'<lyrics>'+'</song>')

f = open("myfile.txt", "w")
f.write('<?xml version="1.0" encoding="utf-8"?>\n'+'<song version="1.0">\n'+'<lyrics language="en">\n'+song_string+'<lyrics>\n'+'</song>')
f.close()

#<?xml version="1.0" encoding="utf-8"?>
# <song version="1.0">
# <lyrics language="en">
# <verse type="custom" label="1"><![CDATA[1 Test 1]]></verse>
# <verse type="custom" label="2"><![CDATA[2 Test 2]]></verse>
# <verse type="custom" label="3"><![CDATA[3 Test 3]]></verse>
# <verse type="custom" label="4"><![CDATA[4 Test 4]]></verse>
# </lyrics>
# </song>

#<?xml version="1.0" encoding="utf-8"?>
# <song version="1.0">
# <lyrics language="en">
# <verse type="custom" label="1"><![CDATA[1 Test 1]]></verse>
# <verse type="custom" label="2"><![CDATA[2 Test 2]]></verse>
# <verse type="custom" label="3"><![CDATA[3 Test 3]]></verse>
# <verse type="custom" label="4"><![CDATA[4 Test 4]]></verse>
# <verse type="custom" label="5"><![CDATA[29 See, some of them today... It's going to get more than ever, and as the days go by, that we're going to see people with this (as Jesus said), " form of godliness,"---and just a form it's coming into. We've had it in the Methodists, and Baptists, and so forth, for years, and now it's creeped over into the Pentecostals. And little...When God gave a man the Holy Spirit He set him with his face towards Calvary, and the Word before him. Now little roots will rise up from off that highway, come in and wrap around and around that tree, and you think it's very innocent. 
#[---]
#But the first thing you know, it's got such a hold on you until it pulls you the wrong way---makes you lean the wrong way. And so has philosophies and things entered among us until it's begun to pull us towards the world. You take the sharp two-edged sword of God and cut free from everything and stay right on that Word, because that is the ultimate. That's the absolute to every believer.]]></verse>
# </lyrics>
# </song>