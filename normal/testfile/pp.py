import csv
# import requests
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
import time


baseurl = 'https://www.google.com/search?q='
pluseurl = input('검색어를 터미널에서 입력하세요 : ')
url = baseurl + urllib.parse.quote_plus(pluseurl)

# add csv file
filename = 'test.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

print(url) # https://www.google.com/search?q=입력데이터(pluseurl)

driver = webdriver.Chrome()
driver.get(url)
print(driver)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
r = soup.select('.tF2Cxc')  #원하는 class / name을 F12에서 찾기 # select 는 list로 가져온다. #클래스는 앞에 . 점 붙여준다.
# r = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
# writer.writerow(r)
# print(r)
# print(type(r)) # <class 'bs4.element.ResultSet'>
# page = 3
num_page = 5
# print(len(r))




# sl = []
# for page in r:
    # print('%s'% page)
    # print(page.text)
    # print(r)
    #
#     # for r in r:
    #     # it1 = r.select_one('.LC20lb.MBeuO.DKV0Md').text
    #     # r안에 a태그 안에 attrs로 원하는 요소 찾아오기
    #     # print(i.text)
    #     # print(i)
    #     temp = []
    #     temp.append(r.a.attrs['href'])
    #     # temp.append(i.a.attrs['href'])
    #     # temp.append(i.text)
    #     # sl.append(temp)
    #     # # it2 = r.a.attrs['href']
    #     # # print(i.text)
    #     # # print(i.a.attrs['href'])
    #     writer.writerow(temp)
    #     # writer.writerow(i.text)

# f.close()

# for page in range(page,num_page):
for page in range(3,4):
    print(page)
#     time.sleep(3)
#     print(int(page))
#     print(int(num_page))
    # for i in range(page) :
    # for i in r:

        # data = (i.select_one('.LC20lb.MBeuO.DKV0Md').text,i.a.attrs['href'])
        # print(len(data))
        # writer.writerow(data)

        # print("data")

    # for i in r :
        # data = (i.select_one('.LC20lb.MBeuO.DKV0Md').text,i.a.attrs['href'])
        # columns = i.find_all('.LC20lb.MBeuO.DKV0Md')
        # columns = (i.select_one('.LC20lb.MBeuO.DKV0Md').text,i.a.attrs['href'])
        # columns = i.select.one('.LC20lb.MBeuO.DKV0Md')
        # dt = [column.text() for column in columns[:]]
        # print(r)
        # writer.writerow(data)

        # print(i.select_one('.LC20lb.MBeuO.DKV0Md').text) #제목 #select one을 사용하면 텍스트를 가져올 수 있다. #클래스에 빈칸은 점으로 바꿔준다.
        # print(i.select('.LC20lb.MBeuO.DKV0Md'))
        # print(i.a.attrs['href'])
        # print(i.a.attrs)
        # print(i.a.attrs['href']) #링크 #a 태그 안에, href 를 속성을 갖는 링크 불루직
        # writer.writerow(i.a.attrs['href'])
    
    # 다음 페이지 클릭
    driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[%s]' %page).click()
    # driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[%s]/a' %page).click()
    # print(page + "page")


#크롬 드라이버 닫아주기
# driver.close()

# 실행 확인
print("\ngood sccess")