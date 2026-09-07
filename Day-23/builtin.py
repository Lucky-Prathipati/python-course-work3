'''
import sys 

print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")
---------------------

import platform 

print(platform.system())
print(platform.release())
print(platform.processor())
------------------------------

import math
print(math.pi)
print(math.e)

print(math.lof(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(8,12))
print(math.sqrt(36))
print(math.pow(2,3))
---------------------------

import math

print(round(12.00000001))
print(round(12.3))
print(round(12.666))
print(round(12.9999999))

print(math.ceil(12.0000000))
print(math.ceil(12.3))
print(math.ceil(12.666))
print(math.ceil(12.9999999))

print(math.floor(12.00000001))
print(math.floor(12.3))
print(math.floor(12.666))
print(math.floor(12.9999999))
---------------------------------

import random 
print(random.random())
print(random.randint(100000,999999))
print(random.uniform(1,6))

l = ['r','p','s']
print(random.choice(l))

lang = ['python','java','css','javascript','flask']
print(random.choices(lang,k=2))

random.shuffle(lang)
print(lang)
------------------------------

from collections import Counter
s = 'python programning'
res = Counter(s)
print(res)
-------------------------------

from collections import Counter,defaultdict

products =['sugar','salt','milk']
res = defaultdict(list)

for i in products:
    res[i].append(['des','rev','com'])

print(res)

                 

s = 'python programing'
d = defaultdict(int)

for i in s:
-------------------------------------------

from collections import Counter,defaultdict,deque

l = deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
-------------------------
'''