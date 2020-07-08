from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


r = requests.get('http://rst.ua/oldcars/poltava/501', headers={'User-Agent':UserAgent().chrome})
html = r.content
soup = BeautifulSoup(html,'html.parser')
obj = soup.find('span', attrs = {'class':'rst-uix-grey'})
print(obj.text)
# for x in soup:
#     # print(x)
    
#     car_name = x.find('a').text
#     print(car_name)
#     # link_to_car = x.attrs['href']