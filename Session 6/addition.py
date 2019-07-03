import requests
import bs4
 
response = requests.get('https://dantri.com.vn/suc-khoe.htm')
 
soup = bs4.BeautifulSoup(response.content.decode(), 'html.parser')
 
all_div = soup.find_all("div", {"data-boxtype": "timelineposition"})
 
result = []
for v in all_div:
    dic = {
        "title": v.div.h2.a.string,
        "img": v.a.img.attrs['src']
    }
    result.append(dic)
 
print(result)
    # result.append(v.div.h2.a.string)
    # print(v.a.img.attrs['src'])
# print(result)
 
 
with open('dantri.html', 'wt', encoding='utf-8') as f:
    f.write(response.content.decode())
 
 
# import time
# from selenium import webdriver
 
# driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# driver.get('google.com')
# time.sleep(5)
# driver.quit()
 
 
# input()