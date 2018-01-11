import MySQLdb
import json


Data = json.load(open('Dec.json'))
print (type(Data))

print(Data[0]['Order ID'])

#for key in Data.keys():
 #   strvalue = str(Data[key].replace("'",'"'))
  #  valuelist.append(strvalue)
#valtuple = tuple(valuelist)
db = MySQLdb.connect('localhost','kumar','Abcd@123','mysql')
cursor1 = db.cursor()
for values in range(0,len(Data)):
    orderid = str(Data[values]['Order ID'])
    description = str(Data[values]['PARTICULARS'])
    debit = str(Data[values]['DR'])
    credit = str(Data[values]['CR'])
    month = str(Data[values]['Month'])
    bal = str(Data[values]['BAL'])
    transdate = str(Data[values]['Tran Date'])
    data = [orderid, transdate, description, debit, credit, bal, month]
    print(data)
    print(orderid, transdate, description, debit, credit, bal, month)
    cursor1.execute('INSERT INTO credit(orderid, transdate, description, debit, credit, bal, month) VALUES(%s,%s,%s,%s,%s,%s,%s)', data)
    db.commit()


try:
    cursor1.execute("select * from credit")
    results = cursor1.fetchall()
    for row in results:
        orderid = row[0]
        description = row[1]
        debit = row[2]
        credit = row[3]
        month = row[4]
        print ("orderid=%s,description=%s,debit=%f,credit=%f,month=%s" %(orderid,description,debit,credit,month))
except:
    print ("Unable to fetch rows")

db.close()