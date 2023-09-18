# themessage
## A tool to display the sermons of William Branham

Goal: To learn how to scrape websites using BeautifulSoup.

Source: https://churchages.net/en/sermons/#branham

### Usage:

Search for sermons by the alphabet:

E.g Searching using the letter "E" should output a list of sermon objects that start with the letter "E"

```
[
{'title': 'The eagle in her nest', 'date': '1957-07-05', 'link': 'https://churchages.net/en/sermon/branham/57-0705-eagle-in-her-nest/'}, 
{'title': 'The eagle stirring her nest', 'date': '1958-05-00', 'link': 'https://churchages.net/en/sermon/branham/58-0500-eagle-stirring-her-nest/'}, 
{'title': 'Early spiritual experiences', 'date': '1952-07-13 Afternoon', 'link': 'https://churchages.net/en/sermon/branham/52-0713A-early-spiritual-experiences/'},
{'title': 'Earnestly contending for the faith', 'date': '1954-04-04 Morning', 'link': 'https://churchages.net/en/sermon/branham/54-0404M-earnestly-contending-for-the-faith/'}
...
]
```