#-*-coding:utf-8-*-
import re
import urllib

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getStory(html):
    pattern=re.compile('【与星团的故事】(.*?)</tbody',re.S)
    result=re.findall(pattern,html)
    for i in result:
        print "【与星团的故事】"+i



url="http://speed.gamebbs.qq.com/forum.php?mod=forumdisplay&fid=30672"
html=getHtml(url)
story=getStory(html)

print story
