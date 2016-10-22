#-*- coding:utf-8 -*-
import re
import csv
import pandas as pd
import numpy as np
name=[]
reply=[]
pv=[]
s=[]
s1="【s1】 heeeee 1 31"
s2="【s2】 haaa 1 37"
s3="【s3】 bdeff 2 23"


s.append(s1)
s.append(s2)
s.append(s2)

for i in s:
    result=i.split()
    name.append(result[0]+result[1])
    reply.append(result[2])
    pv.append(result[3])

data={'Name':name,'Reply':reply,'PageView':pv}
full_data=pd.DataFrame(data)
print full_data
