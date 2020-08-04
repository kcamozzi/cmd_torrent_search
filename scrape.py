import requests
import re
from bs4 import BeautifulSoup

def siteScrape(mySearch, site, page):
        if site == "1337x.to":
                URL = 'https://1337x.to/search/' + mySearch +'/'+ str(page) +'/'
        else:
                print("Unknown Site")

        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        page = requests.get(URL, headers={'User-Agent':user_agent})

        soup = BeautifulSoup(page.content, 'html.parser') 

        results = soup.find("table", class_="table-list table table-responsive table-striped")

        links = results.find_all('a', href=re.compile('/torrent/'))
        
        return links

def listLinks(links):
        for index, link in enumerate(links, start=1):
                print("[", index, "]", link.string, end='\n')

mySearch = input("Search string: ")

pageNum = 1
site = "1337x.to"

links = siteScrape(mySearch, site, pageNum)

listLinks(links)
print("Press n for next page, p for previous page. Press q to quit.")
curCommand = input("Input Command: ")

while curCommand != 'Q' or curCommand != 'q':
        if curCommand == 'n':
                pageNum += 1
                links = siteScrape(mySearch, site, pageNum)
                listLinks(links)
                print("Press n for next page, p for previous page. Press q to quit.")
                curCommand = input("Input Command: ")
        if curCommand == 'p':
                if pageNum == 1:
                        print("Currently on the first page")                
                        print("Press n for next page, p for previous page. Press q to quit.")
                        curCommand = input("Input Command: ")
                else:
                        pageNum -= 1
                links = siteScrape(mySearch, site, pageNum)
                listLinks(links)
                print("Press n for next page, p for previous page. Press q to quit.")
                curCommand = input("Input Command: ")
        


