#%%
# pip install -r requirements.txt
# pip install pandas bs4 selenium webdriver_manager
# %%

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#%%

import sqlite3
from kurlyprs.kprs import getHot,getPdt

#%%
coption= webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=coption)

#%%
# 리뷰 하단의 다음 버튼이 있으면 클릭
pdtcode=5161423
driver=getPdt(pdtcode)

nextButtonCss='#review > section > div.css-1nrf0nk.e1kog1is13 > div.css-jz9m4p.e1kog1is5 > button.css-1orps7k.e1kog1is1'
nextButton=kTarget(driver,nextButtonCss)
print('next button:',nextButton.get_attribute("disabled"))

while (nextButton.get_attribute("disabled")==None):
    print(nextButton.get_attribute("disabled"))
    getReview(pdtcode,driver)
    print('-'*30)
    nextButton.click()
    time.sleep(2)

getReview(pdtcode,driver)
    
#
# %%
