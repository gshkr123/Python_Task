import MySQLdb
import json


Data = json.load(open('OctToApr.json'))
print (type(Data))

print(Data[0]['Tran Date'])

#for key in Data.keys():
 #   strvalue = str(Data[key].replace("'",'"'))
  #  valuelist.append(strvalue)
#valtuple = tuple(valuelist)
db = MySQLdb.connect('localhost','kumar','Abcd@123','mysql')
cursor1 = db.cursor()
for values in range(0,len(Data)):
    #orderid = str(Data[values]['Order ID'])
    description = str(Data[values]['PARTICULARS'])
    debit = int(Data[values]['DR'])
    credit = int(Data[values]['CR'])
    bal = (int(Data[values]['BAL']))
    transdate = str(Data[values]['Tran Date'])
    data = [transdate, description, debit, credit, bal]
    #data = [transdate, description]
    print(data)
    print(transdate, description, debit, credit, bal)
    #cursor1.execute('INSERT INTO CreditAnalysis(Transdate, Description) VALUES(%s,%s)',data)
    cursor1.execute('INSERT INTO CreditAnalysis(Transdate, Description, Debit, Credit, Balance) VALUES(%s,%s,%d,%d,%d)',data)
    db.commit()


db.close()