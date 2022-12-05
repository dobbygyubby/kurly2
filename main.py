#%%
# pip install pandas bs4 selenium webdriver_manager
# %%
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#%%
from bs4 import BeautifulSoup as bs
import sqlite3
from kurlyprs.kprs import getItem,kinsDB

#%%
coption= webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=coption)

#%%
# 목표 요소에 키값 입력하기
def kSendkey(dirver=None ,_selector='',kv=Keys.ENTER):
    src=driver.find_elements(by=By.CSS_SELECTOR,value=_selector)
    src[0].send_keys(kv)
    
def kTarget(dirver=None ,_selector=''):#.click() 을 위한 타겟
    target=driver.find_element(by=By.CSS_SELECTOR,value=_selector)
    return target
        
def kgetBS(thtml='',_tgtsel=''):# bs4를 위한 함수
    soup=bs(thtml,'html.parser')
    elems=soup.select(_tgtsel)
    return elems

# 열린 url로 부터 원하는 요소 반환하기    
def kgetElem(driver,_selector='.css-vjtyom',_tgtsel='div > a'):
    src=driver.find_elements(by=By.CSS_SELECTOR,value=_selector)
    tgtHtml=src[0].get_attribute('outerHTML')
    elems =kgetBS(tgtHtml,_tgtsel)
    return elems

# 스크래이핑을 위해서 url 열기
def kScrap(_srcurl= '',_selector='.css-vjtyom',_tgtsel='div > a'):
    driver.implicitly_wait(10)
    driver.get(_srcurl)
    elems=kgetElem(driver,_selector,_tgtsel)
    return (elems,driver)
#%%
# 컬리로부터 데이터를 수집하여 DB 입력
url='https://www.kurly.com/collections/beauty-nowhot?site=beauty&page=1'
sel='.css-vjtyom'
tsel='div > a'
elems,driver=kScrap(url,sel,tsel)
#kinsDB(elems)
elems[2].text
#%%
# 버튼찾기
url='https://www.kurly.com/goods/5161423'
sel='.css-tse2s2'
tsel='li > a'
elems,driver=kScrap(url,sel,tsel)
print(len(elems))
# 후기클릭
tgtSel='#top > div.css-n48rgu.ex9g73v0 > div.css-16c0d8l.e1brqtzw0 > nav > ul > li:nth-child(3) > a'
kTarget(driver,tgtSel).click()
#%%
## 리뷰 가져오기

def getReview(pdtcode=5161423,driver=None):
    sel='.css-1nrf0nk'
    tsel='div.css-169773r'
    elems=kgetElem(driver,sel,tsel)
    print('****',len(elems))
    for elem in elems:
        #print(elem)
        rev=elem.select('article p')[0].text
        user=elem.select('span.css-f3vz0n')[0].text[0]
        day=elem.select('footer span.css-14kcwq8')[0].text
        revkey=user+day+'_'+str(len(rev))
        print(pdtcode,revkey,rev,day)
        #print(kgetBS(elem,'p'))
#%%
# 리뷰 하단의 다음 버튼이 있으면 클릭
nextButtonCss='#review > section > div.css-1nrf0nk.e1kog1is13 > div.css-jz9m4p.e1kog1is5 > button.css-1orps7k.e1kog1is1'
nextButton=kTarget(driver,nextButtonCss)
print('next button:',nextButton.get_attribute("disabled"))
pdtcode=5161423
while (nextButton.get_attribute("disabled")==None):
    print(nextButton.get_attribute("disabled"))
    getReview(pdtcode,driver)
    print('-'*30)
    nextButton.click()
    time.sleep(2)

getReview(pdtcode,driver)
    
#
# %%
