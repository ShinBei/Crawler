import requests
from bs4 import BeautifulSoup
import sys

def main():
    page=4205;
    while page >= 1:
        #url = 'https://www.ptt.cc/bbs/movie/index4204.html'
        NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a
        response = requests.get("https://www.ptt.cc/bbs/movie/index%s.html" % str(page))
        response.encoding='utf8'
        response.errors='ignore'
        soup = BeautifulSoup(response.text, 'lxml')
        articles = soup.find_all('div', 'r-ent')
        for article in articles:
            meta = article.find('div', 'title').find('a') or NOT_EXIST
            title = meta.getText().strip()
            link = meta.get('href')
            push = article.find('div', 'nrec').getText()
            date = article.find('div', 'date').getText()
            author = article.find('div', 'author').getText()
            
            print(push.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding), title.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding), 
            date.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding),author.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
            
            #print(push, title, date, author)
        page -= 1
        
if __name__ == "__main__":  
    main()
    
    
