import time

import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



db = MySQLdb.connect('localhost','kumar','Abcd@123','mysql')
c = db.cursor()
#wordUsed = 'Python Sentiment'
sql = "SELECT * FROM CreditAnalysis WHERE Description LIKE '%PUR%'"

c.execute(sql)
data = c.fetchall()

print (data)
debit1 = []
credit1 =[]

for i in data:
    debit1 = debit1.append(data[2][i])
    credit1 = credit1.append(data[3],i)
print (debit1, credit1)
print (data[2], data[3])
plt.plot(x=data[2], y = data[3], label = 'Credit Vs Debit', linewidth = 2 )

plt.show()

graphArray = []

for row in c.execute(sql, [(wordUsed)]):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[2]+','+splitInfo[4]
    graphArray.append(graphArrayAppend)

datestamp, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})

fig = plt.figure()

rect = fig.patch

ax1 = fig.add_subplot(1,1,1, axisbg='white')
plt.plot_date(x=datestamp, y=value, fmt='b-', label = 'value', linewidth=2)
plt.show()