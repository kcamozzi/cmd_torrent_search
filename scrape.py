import requests
import re
import os
from bs4 import BeautifulSoup

def siteScrape(mySearch, site, page):
        if site == "https://1337x.to":
                URL = 'https://1337x.to/search/' + mySearch +'/'+ str(page) +'/'
        else:
                print("Unknown Site")

        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        page = requests.get(URL, headers={'User-Agent':user_agent})

        soup = BeautifulSoup(page.content, 'html.parser') 

        results = soup.find("table", class_="table-list table table-responsive table-striped")

        links = results.find_all('a', href=re.compile('/torrent/'))
        
        return links

def findMagnet(URL):
        #URL = "https://1337x.to/torrent/3203168/Eminem-Kamikaze-2018-Mp3-320kbps-Hunter/"
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        page = requests.get(URL, headers={'User-Agent':user_agent})
        soup = BeautifulSoup(page.content, 'html.parser') 
        results = soup.find("a", href=re.compile("magnet"))
        #for result in results:
        os.startfile(results.get('href'))

def listLinks(links):
        for index, link in enumerate(links, start=1):
                print("[", index, "]", link.string, end='\n')
                #print(link.get('href'))

mySearch = input("Search string: ")

pageNum = 1
site = "https://1337x.to"

links = siteScrape(mySearch, site, pageNum)

listLinks(links)
print("Select an index to download magnet link.\nPress n for next page, p for previous page. Press q to quit.")
curCommand = input("Input Command: ")

while curCommand != 'Q' and curCommand != 'q':
        if curCommand == 'n':
                pageNum += 1
                links = siteScrape(mySearch, site, pageNum)
                listLinks(links)
                print("Select an index to download magnet link.\nPress n for next page, p for previous page. Press q to quit.")
                curCommand = input("Input Command: ")
        elif curCommand == 'p':
                if pageNum == 1:
                        print("Currently on the first page")                
                        print("Select an index to download magnet link.\nPress n for next page, p for previous page. Press q to quit.")
                        curCommand = input("Input Command: ")
                else:
                        pageNum -= 1
                links = siteScrape(mySearch, site, pageNum)
                listLinks(links)
                print("Select an index to download magnet link.\nPress n for next page, p for previous page. Press q to quit.")
                curCommand = input("Input Command: ")
        elif curCommand == 't':
                print("Running magnet test...")
                findMagnet()
                curCommand = input("Input Command: ")
        elif int(curCommand) in range(1,20):
                downURL = site + links[int(curCommand) - 1].get('href')
                #print(downURL)
                findMagnet(downURL)
                print("Magnet opening in torrent client...")
                print("Select an index to download magnet link.\nPress n for next page, p for previous page. Press q to quit.")
                curCommand = input("Input Command: ")


        
        


