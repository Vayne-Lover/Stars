#-*-coding:utf-8-*-
import re
import urllib

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
    tool=Tool()
    pattern=re.compile('<font color="#ff0000">(.*?)</p>',re.S)
    result=re.findall(pattern,html)
    for i in result:
        print tool.replace(i)

url="http://speed.gamebbs.qq.com/search.php?mod=forum&searchid=208&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw=【与星团的故事】"
html=getHtml(url)
story=getStory(html)

