# -*- coding: utf8 -*-
from lxml import etree  
import requests  
import sys


def main():
    session = requests.Session()
    #page = 1;
    page='prev';
    stop = 0
    jsonData = "["
    while True:
        #result = requests.get("http://axe-level-1.herokuapp.com/lv2/?page=%s" % str(page))
        result = session.get("http://axe-level-1.herokuapp.com/lv3/?page=%s" % str(page), cookies={'from-my': 'browser'})
        result.encoding='utf8'
        result.errors='ignore'
        root = etree.fromstring(result.content, etree.HTMLParser())
        rows = root.xpath("//table[@class='table']/tr[position()>1]")
        if len(rows) != 10:
            tmp = ""
            for row in root.xpath("//table[@class='table']/tr[position()>1]"):
                column = row.xpath("./td/text()")
                tmp += '{"town": "%s", "village": "%s", "name": "%s"}\n' % (column[0], column[1], column[2])
            jsonData += tmp
            stop = 1
        else:
            tmp = ""
            for row in root.xpath("//table[@class='table']/tr[position()>1]"):
                column = row.xpath("./td/text()")
                tmp += '{"town": "%s", "village": "%s", "name": "%s"}\n' % (column[0], column[1], column[2])
            jsonData += tmp
            page='next';
            #page += 1
        #print(jsonData[0:-1] + "]")
        print(jsonData.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
        #使用 encode 的 replace 功能，把文字改成 "cp950" 的編碼，同時把 "cp950" 不認識的字替換掉 (變成 '?' )，這之後再把它用 "cp950" decode 回去就可以了。
        file = open("python.txt","w")
        file.write((jsonData.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)))
        file.close()
        if stop == 1:
            break

    
    

if __name__ == "__main__":  
    main()