import requests


class Connex:
    url = ''
    data = ''
    status_connection = 'no_connection'
    def __init__(self,url):
        self.url=url

    def check_connection(self):
        r= requests.get(self.url)
        if r.status_code==200:
            self.status_connection = 'established'
            self.data = r.text
        return r.status_code

    def get_data(self):
        if self.status_connection=='established':
            return self.data
        else:
            return "no_connection"