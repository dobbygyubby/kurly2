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
driver.implicitly_wait(10)
srcurl= 'https://www.kurly.com/collections/beauty-nowhot?site=beauty&page=1'
driver.get(srcurl)
# %%
src=driver.find_elements(by=By.CSS_SELECTOR,value='.css-vjtyom')
#%%
tgtHtml=src[0].get_attribute('outerHTML')
print(tgtHtml)
#%%
soup=bs(tgtHtml,'html.parser')
elems=soup.select('div > a')

# 컬리로부터 데이터를 수집하여 DB 입력
kinsDB(elems)
elems[2].text
# %%