import json
import MySQLdb

try:
    db = MySQLdb.connect('localhost', 'kumar', 'Abcd@123', 'mysql')

    cursor1 = db.cursor()
    cursor1.execute("select * from CreditAnalysis where Description Like '%PUR%'")
    results = cursor1.fetchall()
    print (results)
    for row in results:
        transdate = row[0]
        description = row[1]
        debit = row[2]
        credit = row[3]
        bal = row[4]
        print ("transdate = %s,description=%s,debit=%f,credit=%f, bal =%f" %(transdate, description, debit, credit, bal))
except:
    print ("Unable to fetch rows")

try:
    cursor2 = db.cursor()
    cursor2.execute("select sum(Debit) from CreditAnalysis where Description Like '%PUR%'")
    result = cursor2.fetchall()
    print(result[0])
    cursor2.execute("select sum(Debit)/sum(Credit) from CreditAnalysis")
    result3 = cursor2.fetchall()
    print(result3)

except:
    print("No records of PUR Found")