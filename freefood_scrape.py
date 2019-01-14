# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from csv import writer
from datetime import datetime
import pandas

quote_page = 'https://events.ucsb.edu/feature/free-food/'
page = urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

quote_pages = []
divs = soup.findAll('div', attrs={'class':'tax-stuff'})
for div in divs:
    links = div.find('a')
    quote_pages.append(links['href'])

data = []
for pg in quote_pages:
    page = urlopen(pg)

    soup = BeautifulSoup(page, "html.parser")

# name_box = soup.find("h2")

# name = name_box.text.strip()

    names = soup.find('h1')
    names = names.text.strip()
    names = names.replace(',', '+')

    date = soup.find('div', attrs={'id': 'thedates'})
    date = date.text.strip()
    date = str(date)
    date = date.replace(',','+')
    date = date.replace('\n',' ')
    date = date.replace('        ',' ')

    location = soup.find('div', attrs={'id': 'thevenue'})
    location = location.text.strip()

    link = pg

    data.append((names,date,location,link))

df = pandas.DataFrame(data, columns=['Event', 'Date', 'Location' , 'Link'])

# To write the dataframe to a csv file
df.to_csv("static/Output6.csv")
