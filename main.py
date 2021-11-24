import os
import sys
from Connex import *
from Parser import *
import logging
import re


# Include core directory in the module search path
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.realpath(__file__))
#sys.path.append(PARENT_DIR + "/core")

class Scrapper_Soup():
    __instance = None
    name=None
    def __init__(self,name):
        if Scrapper_Soup.__instance!=None:
            raise("This class is singleton")
            
        else:
            Scrapper_Soup.__instance = self
            self.name=name

    @staticmethod
    def get_instance():
        if Scrapper_Soup.__instance is None:
            Scrapper_Soup()
        return Scrapper_Soup.__instance    

    def create_workers(self,types_of_data,urls):
        workers=[]
        for url in urls:
            conn = Connex(url)
            status_code = conn.check_connection()
            if status_code == 200:
                data=conn.get_data()                
                workers.append(Parser(types_of_data,data,url))
        return workers        
        

    def start_workers(self,workers):
        if len(workers) > 0:
            for worker in workers:
                worker.start_work()

    def check_for_formating(self,link):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,link)
        if url:
            return True
        else:
            return False 

    def scan_web(self,filename):
        with open(filename,"r") as f:
            links = f.readlines()

        urls =[]
        for link in links:
            link = link.strip("\n")
            if self.check_for_formating(link):
                urls.append(link)
        workers = self.create_workers('a',urls)
        self.start_workers(workers)

        


def main():
    scrapper1=Scrapper_Soup("WebScrapper")
    scrapper1.scan_web("links")

if __name__=='__main__':
    main()

