import bs4 as bs
import tldextract

class Parser:
    types_of_data =''
    DATA = ''
    soup = None
    file = None

    def __init__(self,typ,data,url):
        self.types_of_data=typ
        self.DATA = data
        self.soup = bs.BeautifulSoup(data,'lxml')
        self.url = url
        self.file =open(Parser.extractDomain(url),"w")
    
    @staticmethod
    def extractDomain(url):
        if "http" in str(url) or "www" in str(url):
            parsed = tldextract.extract(url)
            parsed = ".".join([i for i in parsed if i])
            return parsed
        else: return "NA"

    def start_work(self):
        if self.DATA !='':
            body = self.soup.body
            for links in body.find_all(self.types_of_data):
                self.file.write(f"{links.get('href')}\n")

            