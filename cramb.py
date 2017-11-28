import requests
import re
from bs4 import BeautifulSoup
a = 'http://movie.douban.com/top250/'
def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    # proxy = {  'http': 'http://117.85.105.170:808',
    # 'https': 'https://117.85.105.170:808'}
    data = requests.get(url,headers=headers).content
    return data

def get_data(data):
    soup = BeautifulSoup(data, 'html.parser')
    ol = soup.find('ol', class_='grid_view')
    for i in ol.find_all('li'):
        namelist = i.find('div',class_='hd')
        movie_name = namelist.find('span',class_='title').get_text()
        details = i.find('div',class_='bd')
        score = details.find('span', class_='rating_num').get_text()
        numstar = details.find('div', class_='star')
        numstring = numstar.contents[len(numstar.contents) - 2].get_text()
        num = numstring[:-3]
        des = details.find('span',class_='inq').get_text()
        print movie_name
        print score
        print num
        print des
    if soup.find('span',class_='next').find('a')['href']:
        next = soup.find('span',class_='next').find('a')['href']
        return next
data = get_url(a)
next = get_data(data)
while next:
    url = a + next
    data = get_url(url)
    next = get_data(data)



