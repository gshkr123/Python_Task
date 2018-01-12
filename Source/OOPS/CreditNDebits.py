
class Account(object):

    def __init__(self, holder, number, balance, credit = 1500):
        self.holder = holder
        self.number = number
        self.credit = credit
        self.balance = balance

    def deposit(self, amount):
        self.balance = amount

    def withdraw(self, amount):
        if(self.balance- amount < -self.credit):
            #Coverage Insuffecient
            return False
        else:
            self.balance -=amount
            return True

    def balance(self):
        return self.balance

    def transfer(self, target, amount):
        if(self.balance - amount <-self.credit):
            #Coverage Insuffecient
            return False
        else:
            self.balance -=amount
            target.balance +=amount
            return True

    #if __name__ == ('__main__'):
k1 = Account("Kumar", 33355, 45000)
k2 = Account("Raja", 33356, 25000)

acc1Bal = k1.balance
acc2Bal = k2.balance
transferAcc1toAcc2 = k1.transfer(k2, 5000)
        
print ("Before Transfer Account Balance1 ="+ str(acc1Bal) + " Account Balance2 = " + str(acc2Bal))
print ("Is the Transfer Completed " + str( transferAcc1toAcc2))
acc1Bal =k1.balance
acc2Bal =k2.balance

print ("After Transfer Account Balance1 ="+ str(acc1Bal) + " Account Balance2 = " + str(acc2Bal))

        
