import requests
import bs4
response = requests.get('https://dantri.com.vn')
# print(response.content.decode())
soup = bs4.BeautifulSoup(response.content.decode(),'html.parser')

# print(soup.title)
all_div = soup.find_all("div",{"data-boxtype":"timelineposition"})


print(len(all_div))
with open('dantri.html', 'wt', encoding='utf-8') as f:
    f.write(response.content.decode())

