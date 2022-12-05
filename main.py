#%%
# pip install pandas bs4 selenium webdriver_manager
# %%
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
    
def kClick(dirver=None ,_selector=''):
    driver.find_element(by=By.CSS_SELECTOR,value=_selector).click()
        
    
# 열린 url로 부터 원하는 요소 반환하기    
def kgetElem(driver,_selector='.css-vjtyom',_tgtsel='div > a'):
    src=driver.find_elements(by=By.CSS_SELECTOR,value=_selector)
    tgtHtml=src[0].get_attribute('outerHTML')
    print(tgtHtml)
    soup=bs(tgtHtml,'html.parser')
    elems=soup.select(_tgtsel)
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
tgtSel='#top > div.css-n48rgu.ex9g73v0 > div.css-16c0d8l.e1brqtzw0 > nav > ul > li:nth-child(3) > a'
kClick(driver,tgtSel)
#%%
## 리뷰 가져오기
sel='.css-1nrf0nk'
tsel='div > article'
elems=kgetElem(driver,sel,tsel)
print('****',len(elems))


#
# %%
