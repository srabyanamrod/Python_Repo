class stuff:
    raise_ratio = 1.8
    stuffCounter = 0
    def __init__(self,name,surname,salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + surname + "@asd.com"
        stuff.stuffCounter += 1

    def giveNameSurname(self):
        print(self.name + self.surname)

    def ratio(self):
        self.salary = self.salary + self.raise_ratio*self.salary

personel1 = stuff("Murat", "Celiktepe", 100)
personel2 = stuff("Murat", "Celiktepe", 200)
print(personel1.salary)
personel1.ratio()
print(int(personel1.salary))
print(stuff.stuffCounter)
