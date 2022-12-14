from person import Person

def main():
    person1 = Person('Bärbaum', 'Anita', 78100)
    person1.set_organization('Sales')
    person1.set_supervisor('')
    person1.print()


if __name__ == "__main__":
    main()

   

    

    
"""

class Employee(Person):

    def __init__(self, wageClass, wageLevel):
        Person.__init__(self, self.__name, self.__firstname, self.__personalid)
        __supervisor = Person.get_supervisor(self)
        __organization = Person.get_organization(self)
        self.__wageClass = wageClass
        self.__wageLevel = wageLevel

    def get_wageClass(self):
        return self.__wageClass

    def get_wageLevel(self):
        return self.__wageLevel   

    def __increaseWageClass(wageClass):
        if wageClass < 30:
            wageClass = wageClass + 1
        elif wageClass > 1:
            wageClass = wageClass + 1
        #is this correct?    
        else:  print("Employe:", self.__fristname, self.__name, "has reached the limit of the available wage classes."  )

        return wageClass

    def __increaseWageLevel(wageLevel):
        if wageLevel < 30:
            wageLevel = wageLevel + 1
        elif wageLevel > 1:
            wageLevel = wageLevel + 1
        #is this correct?    
        else:  print("Employe:", self.__fristname, self.__name, "has reached the limit of the available wage levels."  )

        return wageLevel

    def __get_YearlySalary(self):
        wageClass = self.get_wageLevel(self)
        wageLevel = self.get_wageLevel(self)

        salary = 48000 + wageClass * 7000 + wageLevel * 750
        return salary


class Hourlywage(Person):
    def __init__(self):
        Person.__init__(self, self.__name, self.__firstname, self.__personalid)
      
    def get_hourlyWage(self):
        return self.__hourlyWage

    def set_hourlyWage(self, value):
        self.__hourlyWage


        """