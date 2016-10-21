#-*-coding:utf-8-*-
import re

s="【与星团的故事】 犹如痴呆般的傻苏 1 31"
a=re.findall(r"(.*) ",s)
pattern1=re.compile(r'【(.*) ')
pattern2=re.compile(r'\D')
pattern3=re.compile(r' +\d')
b=re.sub(pattern1,"",s)
c=re.sub(pattern2," ",s)
d=re.sub(pattern3,"",c)
e=s.split()
#print "".join(a)
a=e[0]
b=e[1]
c=e[2]
d=e[3]
print a,b,c,d
