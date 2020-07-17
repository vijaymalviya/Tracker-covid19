from django.shortcuts import render
import requests
import bs4

def index(req):
    url = "http://www.mohfw.gov.in/"
    data = requests.get(url)
    bs = bs4.BeautifulSoup(data.text,'html.parser')
    info = bs.find("div",class_="site-stats-count")
    print(info)
    return render(req,'index.html')
    

	




# Create your views here.
