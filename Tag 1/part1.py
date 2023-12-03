import re

sum=0
f = open('Input.txt','r')
for l in f:
     sum+=int(re.findall('(\d)',l)[0]+re.findall('(\d)',l)[-1])
print(sum)