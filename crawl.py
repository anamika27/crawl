import requests
from bs4 import BeautifulSoup


def crawl(url, word):
    page = 1
    count = 0
    while page <= 5:
        src = requests.get(url)
        req = src.text #required shit
        parse = BeautifulSoup(req, 'html.parser')
        for para in parse.body.find_all('p'):
            count += para.text.count(word)
        page += 1
        print(str(count) + ' ' + str(page)) 
        for link in parse.findAll('span', {'class': 'reference-text'}):
            for ref in link.findAll('a', {'class' : 'external text'}):
                l = str(ref.get('href'))
                if l[0] == '#' or l.endswith(".pdf") or 'books.google.com' in l:
                    continue
                elif l.startswith('http'):
                    crawl(l, ' ')
                    page += 1
                elif l[0] == '/':
                    crawl(l[2:], ' ')
                    page += 1
        

           
word = str(input())        
crawl('https://en.wikipedia.org/wiki/' + word, word)
