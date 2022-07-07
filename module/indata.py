import time
import pandas as pd
from format import *
import csvmodule as cm
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# 로그인확인도 해야함

def urldata():
    curl = driver.current_url
    url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'  
    
    if url == curl:
        print("good")
    elif url != curl:
        url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
        driver.get(url)
        driver.implicitly_wait(5)

    file = "data.csv"
    df = pd.read_csv(file, sep='\t', names=["href: "])
    
    at = []
    gab = []
    
    for i in df.index:
        print(i)
        driver.find_element(By.XPATH, """//*[@id="radio1"]""").click()

        inurl = driver.find_element(By.ID, "acuseUrl")
        inurl.clear()

        inurl.send_keys(df.loc[i])
        driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
        time.sleep(1)

        at.append(Alert(driver).text)
        Alert(driver).accept() # ALERT 확인 누르기

        if 'URL' in at[i]:
            gab.append("GOOD")
        else:
            gab.append("BAD")


        inurl.clear()
        time.sleep(1)

    dataf = pd.DataFrame(cm.writer, columns=['URL'])
    dataf['GAB TEXT'] = at
    dataf['GOOD AND BAD'] = gab
    dataf.to_csv("3.GAB FILE.csv", index=True, encoding="utf-8-sig")










# 6번째 에서 3,2 번 순으로 라디오 버튼을 클릭함 원인을 모르겠음.. -> url에 트위터가 찍혀 있어서 바뀌였던거.


# 추가 기능 1 = 트위터, 페이스북, 유튜브, 인스타 등 거르기 -> db를 만들어서 db안에 있는지 확인 후 
# 추가 기능 2 = 사용 가능한 url 또는 이미 사용 중인 url 찾아서 분류 하기 -> 하고 있는중 