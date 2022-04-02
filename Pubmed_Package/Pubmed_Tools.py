from bs4 import BeautifulSoup as bs
import requests

def get_title(link):
    page = requests.get(link)
    content = bs(page.content,features="lxml")
    content = content.find_all(class_='heading-title')
    info = [i.text for i in content]
    info = info[0]
    info = info.replace('\n','')
    info = info.strip()
    return info
    
def get_first_author(link):
    page = requests.get(link)
    content = bs(page.content,features="lxml")
    content = content.find_all(class_='full-name')
    info = [i.text for i in content]
    info = info[0]
    return info
    
def get_date(link):
    page = requests.get(link)
    content = bs(page.content,features="lxml")
    content = content.find_all(class_='cit')
    info = [i.text for i in content]
    info = info[0]
    return info
    
def get_doi(link):
    page = requests.get(link)
    content = bs(page.content,features="lxml")
    content = content.find_all(class_='citation-doi')
    info = [i.text for i in content]
    info = info[0]
    info = info.replace('\n','')
    info = info.strip()
    return info

