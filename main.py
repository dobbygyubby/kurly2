#%%
# pip install pandas bs4 selenium webdriver_manager
# %%
from selenium import webdriver
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

def kscrap(_srcurl= 'https://www.kurly.com/collections/beauty-nowhot?site=beauty&page=1',_selector='.css-vjtyom',_tgtsel='div > a'):
    driver.implicitly_wait(10)
    driver.get(_srcurl)
    src=driver.find_elements(by=By.CSS_SELECTOR,value=_selector)
    tgtHtml=src[0].get_attribute('outerHTML')
    print(tgtHtml)
    soup=bs(tgtHtml,'html.parser')
    elems=soup.select(_tgtsel)
    return elems
#%%
# 컬리로부터 데이터를 수집하여 DB 입력
url='https://www.kurly.com/collections/beauty-nowhot?site=beauty&page=1'
sel='.css-vjtyom'
tsel='div > a'
elems=kscrap(url,sel,tsel)
#kinsDB(elems)
elems[2].text
#%%

url='https://www.kurly.com/goods/5161423'
sel='.css-tse2s2'
tsel='li > a'
elems=kscrap(url,sel,tsel)
print(len(elems))

# %%
url='https://www.kurly.com/goods/5161423'
sel='.css-1nrf0nk'
tsel='div > article'
elems=kscrap(url,sel,tsel)
print(len(elems))
#
# %%
