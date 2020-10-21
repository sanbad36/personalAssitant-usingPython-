import bs4
import myAssistant as a
import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def GiveNews():
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    # Print news title, url and publish date
    a.speak ("How much total top newsfeeds heading  you want to listen ")
    cnt1=a.takeCommand().lower()
    cnt=int(cnt1)
    print(f"\n------------- Showing Top {cnt} News  ---------------\n")
    count=0
    for news in news_list:
        if count<3:
            
            print(news.title.text)
            print(news.pubDate.text)
            a.speak(news.title.text)
            print("-"*60)
            count += 1
            time.sleep(3)
            
        else:
            a.speak('Done telling the news sir ')
            break
        
