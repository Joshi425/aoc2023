import re

digits = [ "zero","one","two","three", "four", "five", "six", "seven", "eight", "nine"]

sum=0
f = open('Input.txt','r')
for l in f:
     for d,digitstr in enumerate(digits):
          l=l.replace(digitstr,digitstr+str(d)+digitstr)
     print(l)
     print(re.findall('(\d)',l)[0]
          +re.findall('(\d)',l)[-1])
     sum+=int(
          re.findall('(\d)',l)[0]
          +re.findall('(\d)',l)[-1]
          )
print(sum)