#%%

from kurlyprs.kdb import selBT
rows=selBT("breview",'limit 1')
print(rows)
# %%
# JDK 설치 
# https://www.oracle.com/java/technologies/downloads/#jdk19-windows
# pip install konlpy
from konlpy.tag import Kkma
kkma=Kkma()
pos=kkma.pos("안녕하세요 여러분")
pos

# %%
