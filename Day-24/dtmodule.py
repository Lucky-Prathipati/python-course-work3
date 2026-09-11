'''
from datetime import date,time,datetime,timedelta

t = date.today()

print(t)
print(t.day)
print(t.month)
print(t.year)
print(t.weekday())

year,month,day = list(map(int,input('[YYY-MM-DD]').split('-')))
print(date(year,month,day))
-------------------------------------------

from datetime import date,time,datetime,timedelta

t = date.today()

tm = time(23,6,6)

print(tm)
print(tm.hour)
print(tm.minute)
print(tm.second)
---------------------------------

from datetime import date,time,datetime,timedelta

dt = datetime.now()
print(dt)
print(dt.strftime('%d-%m-%y'))
print(dt.strftime('%d-%m-%Y'))
print(dt.strftime('%d-%m-%Y %H:%M:%S'))
print(dt.strftime('%d-%m-%Y %H:%M:%S %p'))
print(dt.strftime('%d-%m-%Y %I:%M:%S %p'))
print(dt.strftime('%d-%b-%Y %I:%M:%S %p'))
print(dt.strftime('%d-%B-%Y %I:%M:%S %p'))
print(dt.strftime('%a, %d-%B-%Y %I:%M:%S %p'))
print(dt.strftime('%A, %d-%B-%Y %I:%M:%S %p'))
------------------------------------------------

from datetime import date,time,datetime,timedelta

dt = datetime.now()
t = date.today()

t7 = + timedelta(days=7)

m15 = dt+ timedelta(minutes=15)
print(t7,m15)
-----------------------------------
'''
from datetime import date,time,datetime,timedelta

from itertools import permutations,combinations

s = 'abc'

res1 = list(permutations(s,2))
res2 = list(combinations(s,2))

print(list(permutations(s,2)))
print(list(combinations(s,2)))





