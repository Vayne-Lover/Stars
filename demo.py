#-*-coding:utf-8-*-
import re
import csv
import urllib
import numpy as np
import pandas as pd

class Tool:
    pattern1=re.compile('次查看')
    pattern2=re.compile('个回复 - ')
    pattern3=re.compile('</font(.*?)ong>')
    pattern4=re.compile('</a>(.*?)="xg1">',re.S)

    def replace(self,x):
        x=re.sub(self.pattern1,"",x)
        x=re.sub(self.pattern2,"",x)
        x=re.sub(self.pattern3," ",x)
        x=re.sub(self.pattern4," ",x)
        return x.strip()

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getStory(html):
    name=[]
    reply=[]
    pv=[]
    tool=Tool()
    pattern=re.compile('<font color="#ff0000">(.*?)</p>',re.S)
    res=re.findall(pattern,html)
    for i in res:
        result=tool.replace(i)
        result=result.split()
        j=0
        nameAppend=""
        while not(result[j].isdigit()):
            j+=1
        for k in range(0,j):
            nameAppend+=result[k]
        name.append(nameAppend)
        assert j<=len(result)-2
        reply.append(result[j])
        pv.append(result[j+1])
    data={'Name':name,'Reply':reply,'PageView':pv}
    full_data=pd.DataFrame(data)
    full_data.to_csv('data.csv', index=True)


url="http://speed.gamebbs.qq.com/search.php?mod=forum&searchid=131&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw=【与星团的故事】"
html=getHtml(url)
story=getStory(html)

