print(" Welcome to Budget Tracker application \n Please provide your details:")
name = input("Your Name:")
age = int(input("Age:"))
email = input("Your email")
num = int(input("Your mobile number"))
SSN = int(input("Enter your SSN"))
lim = int(input("Enter tracking limit amount"))
#__init__ constructor and self are implemented in every class.
#class 1 created
class Details():
    def __init__(self, n, a, e, nu):
        self.name = n
        self.age = a
        self.email = e
        self.num = nu

    def details(self,s):
        self.__ssn = s        #private variable used here
        print("\n Name: ", self.name + "\n Email: ", self.email)
        print(" Age:", self.age)
        print(" Mobile no.:", self.num)
        print(" SSN:", self.__ssn)
#class 2, Inheritance and super implemented
class Income(Details):
    income = 0

    def __init__(self, n, a, e, nu):
        super(Income, self).__init__(n, a, e, nu)  #super implemented here

    def upd_salary(self):
        self.a = int(input("Enter your savings"))
        self.__class__.income = self.__class__.income + self.a
        print("Total savings: ", self.__class__.income)
#class 3, Ineritance implemented
class Addexp(Details):
    a = 0

    def __init__(self, n, a, e, nu):
        Details.__init__(self, n, a, e, nu)

    def upd_exp(self):
        b = []
        c = int(input("Enter the number of expenses you want to add:"))
        for x in range(0, c):
            t = int(input("Add your expense here "))
            b.append(t)
        print("List of expenses added", b)
        self.exp = sum(b)
        self.__class__.a = self.__class__.a + self.exp
        print("Sum of expenses added:", self.__class__.a)

#class4, multiple Inheritance implemented below
class Balance(Addexp, Income):
    bal = 0
    def __init__(self):
        print("Check your balance here:")
    def bala(self):
        self.__class__.bal = Income.income - Addexp.a
        print("Total Savings:",Income.income)
        print("Total Expenses:", Addexp.a)
        print("Amount Left:", self.__class__.bal)

#class 5, Inheritance implemented
class Tracking(Balance):
    def __init__(self, l):
        self.tr = l
        if (Balance.bal < self.tr):
            print("Your remaining balance:",Balance.bal)
            print("Your balance is less than your set limit")
        elif (Balance.bal > self.tr):
            print("Your remaining balance:", Balance.bal)



a = Details(name, age, email, num)
a.details(SSN)
b = Income(name, age, email, num) #Instance of class Income 'b' is created and it extends instance of class Details 'a'
b.upd_salary()  #updating income of instance 'b'
c = Addexp(name, age, email, num)  #Instance of class Addexp 'c' is created and it extends instance of class Details 'a'
c.upd_exp()  #updating expenses of instance 'c'
d = Balance() #Instance of class Balance 'd' is created and it extends instance of classes Income 'b' and Addexp 'c'
d.bala()  #checking balancing with the instance 'd'
e = Tracking(lim) #Instance of class Tracking 'e' is created and it extends instance of class Balance 'd'

b.upd_salary()
c.upd_exp()
d.bala()
e.__init__(lim)
