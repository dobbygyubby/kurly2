#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re
from kurlyprs.kdb import selBT,selSQL
#%%
rows=selBT("breview",'limit 1,2','review')
print(rows)
# %%
# JDK 설치 
# https://www.oracle.com/java/technologies/downloads/#jdk19-windows
# pip install konlpy

from konlpy.tag import Kkma
#%%

#bow Bag of words
#%%
def makeWdict(senten):
    kkma=Kkma()
    pos=kkma.pos(senten)
    pocate=['NNG','NNP','NNB','NNM','VV','VA','VCP','VCN']
    wdict={}
    for po in pos:
        if(po[1] in pocate):
            print(po[0])
            if po[0] in wdict.keys():
                wdict[po[0]]+=1
            else:
                wdict[po[0]]=1
            wdf=pd.DataFrame(data=list(wdict.items())).set_index(0)
    return wdf

# %%
def reSEN(sen):
    pattern='[^ㄱ-힣a-zA-Z0-9 .!?]'
    return re.sub(pattern,'',sen)

rows=selBT("breview",'limit 20','review')
mdf=pd.DataFrame()
for r in rows:
    sen=reSEN(r[0])
    sdf=makeWdict(sen)
    print(sdf.index)
    mdf=pd.merge(mdf,sdf,how='outer', left_index=True, right_index=True,)
mdf.fillna(0)

# %%
plt.imshow(mdf.values)
# %%
# SELECT a.id,substr(b.date,0,8) month,sale,title,count(rkey) cnt from beauty a 
# left join breview b on a.pcode=b.pcode
# where a.id=93 
# group by a.id,substr(b.date,0,8)
# order by b.date asc
tbl='beauty a left join breview b on a.pcode=b.pcode'
whr='where a.id=93 group by a.id,substr(b.date,0,8) order by b.date asc'
cols='a.id,substr(b.date,0,8) month,sale,title,count(rkey) cnt'
rows=selBT(tbl,whr,cols)
rdf=pd.DataFrame(rows,columns=['id','month','sale','title','cnt'])
rdf[['month','cnt']].plot()

# %%
msql=""" 
SELECT substr(b.date,0,8) month,count(rkey) cnt from 
 beauty a left join breview b on a.pcode=b.pcode 
 where a.id={} group by substr(b.date,0,8) order by b.date asc
"""
# %%
sql=""" 
SELECT a.id,count(rkey) cnt from beauty a 
 left join breview b on a.pcode=b.pcode 
 group by a.id
 order by cnt desc
 limit 10
"""
df=pd.DataFrame()
for r in rows:
    rows=selSQL(msql.format(r[0]))
    mdf=pd.DataFrame(rows)
    #df=pd.merge(df,mdf,how='outer',left_index=True,right_index=True)
# %%
