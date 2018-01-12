import datetime

class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname, height, birthdate):
        self.name = name
        self.surname = surname
        self.height = height
        self.birthdate = birthdate
        self._age = None
        self._age_last_recalculated = None
        self._recalculate_age()

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def fullname(self): # instance method
       
        return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
        
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith): # static method
            
        return [t for t in Person.TITLES if t.endswith(endswith)]

    @property
    def fullname(self):
        return "%s %s" % (self.name, self.surname)

    def age(self):
        if(datetime.date.today > self._age_last_recalculated):
            self._recalculate_age()

        return self._age

    def _recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age-=1
        self._age = age
        self._age_last_recalculated = today

kumar = Person("Kumar", "Raja", 155, datetime.date(2015, 12, 1))
kumar.height+=3
kumar.set_height(kumar.height+1)

print(kumar.fullname)

print(kumar.height)

print (kumar._age)

print(kumar.allowed_titles_starting_with("M"))
print(Person.allowed_titles_starting_with("M"))

print(kumar.allowed_titles_ending_with("s"))
print(Person.allowed_titles_ending_with("s"))
