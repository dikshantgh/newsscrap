#!/usr/bin/python3
from tqdm import tqdm
import time
import socket
import datetime
import urllib.request
from urllib.request import URLError
def ping_test():
    def bar():
       for k in tqdm(range(100)):
          time.sleep(0.03)

    
    url =[]
    for k in range(3):
        url.append((input("enter url   in format:\n")).lower())
    bar()
    while True:
     for i in range(3):
        url[i]= url[i].replace("https://","http://")   
        if ("http://")  not in url[i]:
            url[i] = "http://"+url[i]
        f = open("log.txt","a")
        dt=datetime.datetime.now().isoformat()

        try:
            web = urllib.request.urlopen(url[i], timeout=5)
            f.write("%s --%s site working\n" %(dt,url[i]))
            print("%s--site working\n"%(url[i]))
    
        except Exception as e:
            f.write("%s -- %s --%s link\n"%(dt,url[i],e))
            print(e,"\n")
            print("%s---\n" %(url[i]) )
     time.sleep(2)       
   

if __name__ == "__main__":
 
    ping_test()
    
