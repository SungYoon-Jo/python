import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import time
import urllib.parse
import webbrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# selenium 안에 webdriver를 사용하기 위해서 웹 사이트를 띄운다


# csv파일로 저장 할수 있도록 한다. 이름, 파일 데이터 형태, 저장 순으로 초기화 해준다.
filename = 'google.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

con = 0

# num = int(input("10단위로 입력해주세요 : "))
num = 10

# con = 0 부터 num 30까지 10씩 증가하며 반복 0 = 1p 10 = 2p 20 = 3p ...
for pg in range(con,num,10):
    print(pg)
    # url = "https://www.google.com/search?q=apple&ei=CKmVYveQMpqJoAS7xbuQAg&start=%d&sa=N&ved=2ahUKEwj3tIuUgon4AhWaBIgKHbviDiIQ8tMDegQIAxA9&biw=1036&bih=666&dpr=1.25"% pg #소스페이지
    if (pg == 0):
        # pluseurl = input('검색어를 터미널에서 입력하세요 : ')
        pluseurl = "온라인바카라"
        url = 'https://www.google.com/search?q=%s' %(pluseurl)
        driver = webdriver.Chrome()    

    ch = "&start=%d" % (pg)
    churl = url + ch
    driver.get(churl)
    # time.sleep(4)
    wait = WebDriverWait(driver,5)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    # r = soup.select('.tF2Cxc > .yuRUbf') 
    r = soup.select('.tF2Cxc') 
    # TbwUpd, B6fmyf, tF2Cxc, NJjxre
    # writer.writerow(r)



    # temp.append("href","text")
    # temp = "href"
    for i in r:
        temp = []
        # print(i)
        # temp[i].append(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
        temp.append(i.a.attrs['href'])
        # temp.append(i.attrs['text'])
        # temp.append(i.text)
        # name = i.select_one('text')
        # temp.append(temp)

        # temp = i.a.attrs['href']
        # print(temp)
        # print(temp[0:10])
        # print(len(temp))
        writer.writerow(temp)
        # webbrowser.open(temp)
        # 0번째 웹 url 열기, 문제: 한개만 여는것이 아니라 한번에temp[1]의 내용을 열어버림, 해결책: 하나씩 열어서 하나씩 닫아야함 또한 url을 하나씩 할당 해줘야함
        # 한개를 누르고 사진을 받아오고 닫고 다음거 누르고 받고 닫고

#크롬 드라이버 닫아주기
driver.close()

# 그냥 실행 확인
print("\ngood sccess")

# 추가 해야 할 기능 
# click url and inside url 캡처

# 참고 자료

# for i in r:
#     temp = []
#     temp.append(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
#     # print(temp)
#     writer.writerow(temp)

#     temp.append(i.a.attrs['href'])
#     # print(temp)
#     writer.writerow(temp)

# for i in r:
#     print(len(temp))