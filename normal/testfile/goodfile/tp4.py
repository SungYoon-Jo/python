from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# bluetooth 오류 제거
# options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


while 1:
    q = input('목록을 선택해주세요 bye, login, put : ')

    if q == "bye":
        break

    elif q == "login": #로그인 정보가 맞지 않았을때 텍스트를 불러오고 다시 입력 할 수 있도록 하는 기능 추가 하기.
        url = 'https://www.nuricops.org/index.do'
        # driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.implicitly_wait(5)

        login = driver.find_element(By.ID, "memberId")
        myid = input('아이디를 입력해주세요 : ')
        login.send_keys(myid)
        mypw = input('패스워드를 입력해주세요 : ')
        login = driver.find_element(By.ID, "memberPw")
        login.send_keys(mypw)
        driver.find_element(By.XPATH, """//*[@id="btnMemberloginCheck"]""").click()
        driver.implicitly_wait(5)

        url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
        driver.get(url)



    elif q == "put":

        driver.find_element(By.XPATH, """//*[@id="radio1"]""").click()

        file = "google.csv"
        df = pd.read_csv(file, sep='\t', names=["href"])

        aet = list()

        for i in df.index:
            print(i)
            inurl = driver.find_element(By.ID, "acuseUrl")
            inurl.send_keys(df.loc[i])
            driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
            time.sleep(2)

            aet.append(Alert(driver).text)
            Alert(driver).accept()
            time.sleep(2)
            inurl.clear()

            print(aet[i])
            print()

# 중복확인까지 가능 현재 
# 추가 사항 원시 url 크롤링 하기 이유 : 정제되지 않은 url을 넣어서 확인 하다 보니 url확인 요청 문구가 너무 많이 뜸

