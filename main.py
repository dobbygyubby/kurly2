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
#print(len(elems))
#%%
def getItem(elem):
    pdtcode=elem.attrs['href'].replace('/goods/','')
    
    couponElem=elem.select('.css-w9ezyo')
    #print(couponElem)
    if(len(couponElem)>0):
        coupon=couponElem[0].text.replace('%쿠폰','').replace('+','').strip()
    else:
        coupon=0
    # 타이틀
    titleElem=elem.select('.css-rklo75')
    if(len(titleElem)>0):
        title=titleElem[0].text
    else:
        title='no name'
    # 디스카운트        
    discElem=elem.select('.discount-rate')
    if(len(discElem)>0):        
        disc=discElem[0].text.replace('%','').strip()
    else:
        disc=0
    # 판매가
    priceElem=elem.select('.sales-price')
    if(len(priceElem)>0):
        price=priceElem[0].text.replace('원','').replace(',','').strip()
    else:
        price=0
    # 정가
    oriElem=elem.select('.dimmed-price')
    if(len(oriElem)>0):
        oriprice=oriElem[0].text.replace('원','').replace(',','').strip()
    else:
        oriprice=price
    return ('hot',pdtcode,coupon,title,disc,price,oriprice)
# %%
print(getItem(elems[0]))
# %%
dbfile='data\kurly.db'
def selBT():
    sql='select * from beauty'
    with sqlite3.connect(dbfile) as conn:
        cur=conn.cursor()
        cur.execute(sql)
        rows=cur.fetchall()
    print('*'*30)
    for row in rows:
        print(row)

# %%

#data=('hot','1000074086', '10', '[아틀리에 코롱] 클레망틴 캘리포니아 코롱 압솔뤼 30ml', '15', '97750', '115000')
def insBT(data):
    inssql='insert into beauty (cate,pcode,coupon,title,sale,price,oriprice) \
        values(?,?,?,?,?,?,?)'
    with sqlite3.connect(dbfile) as conn:
        cur=conn.cursor()
        cur.execute(inssql,data)
#%%
print(len(elems))
#%%
# 크롤링하여 DB에 넣기
i=0
for elem in elems:
    i+=1
    #print(i)
    data=getItem(elem)
    insBT(data)
    print(".",end='')
# %%
elems[2].text
# %%