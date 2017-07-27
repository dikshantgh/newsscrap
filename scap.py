#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib.request
import socket
import time
from tqdm import tqdm
from urllib.request import URLError
def site_test():
    def bar():
        for k in tqdm(range(100)):
            time.sleep(0.009)
    url = input("enter the url,in  format:\n").lower()
    
    url =url.replace('https://','http://')
    if ("http://") not in url:

        url = "http://"+url
    bar()
    try:
        page = urllib.request.urlopen(url, timeout=7)
        soup= BeautifulSoup(page,'lxml')
        k=0
        if "ekantipur" in (soup.find('title').text):
           
           for i in soup.find_all('div',class_ ="display-news-title"):
               k=k+1
               if k==11:
                    break
               z=i.find('a').text
               print(k,")",z,"\n")
                

           
        if "Ratopati" in (soup.find('title').text):
         
           for i in soup.find_all('div',class_ ="item-content"):
                k=k+1
                if k==11:
                    break
                z=i.find('a').text
                print(k,")",z,"\n")


        if "Light Nepal" in (soup.find("title").text):

           for i in soup.find_all("div",class_ ="main-list small-list clearfix"):
                k=k+1
                if k==11:
                    break
                z=i.find('a').text
                print(k,")",z,"\n")
                                       
        if "BigulNews" in (soup.find('title').text):
        
            for i in soup.find_all('h3',class_ ="entry-title td-module-title"):
                k=k+1
                if k==11:
                    break
                z=i.find('a').text
                print(k,")",z,"\n")
                                       

        if "recent" in (soup.find('title').text):

            for i in soup.find_all('h4',class_ ="news-title"):
                k=k+1
                if k==11:
                    break
                z=i.find('a').text
                print(k,")",z,"\n")
    
        if k==0 :
            print('not a listed site for scrapping')

    except Exception as ex :
        print(ex)
if __name__ == "__main__":
    site_test()
