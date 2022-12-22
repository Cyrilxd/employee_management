from employe import Employe

class PermanentEmployee(Employe):

    def __init__(self, lastName, firstName, personalid, wageClass, wageLevel):
        """Initializes a new permanent employe object with the given values and validation"""
       
         #V alidate given parameter types
        if not isinstance(wageClass, int):
            raise ValueError(wageClass, 'has the wrong type. The given type needs to be int.')
        if wageClass > 30 or wageClass < 0:
            raise ValueError('Wageclass needs to be a number between 0 and 30.')
        if not isinstance(wageLevel, int):
            raise ValueError(wageLevel, 'has the wrong type. The given type needs to be int.')
        if wageLevel > 20 or wageLevel < 0:
            raise ValueError('Wagelevel needs to be a number between 0 and 20.')   

        # Initialize Parent Compoenent
        super().__init__(lastName, firstName, personalid)
    
        # Initialize Class properties
        self.__wageClass = wageClass
        self.__wageLevel = wageLevel

    # get method for the wage class parameter 
    def get_wageClass(self):
        return self.__wageClass

    # get method for the wage level parameter 
    def get_wageLevel(self):
        return self.__wageLevel   

    # method to increase the wage class value 
    def increaseWageClass(self):
        if self.__wageClass < 30:
            self.__wageClass =  self.__wageClass + 1
        else:   raise Exception("Employe:", self.__lastName, self.__firstName, "has reached the limited number of 30 of the available wage classes and can't be updated.")

    # method to increase the wage level value 
    def increaseWageLevel(self):
        if self.__wageLevel < 20:
            self.__wageLevel = self.__wageLevel + 1
        else:   raise Exception("Employe:", self.__lastName, self.__firstName, "has reached the limited number of 20 of the available wage classes and can't be updated.")

    # get method for the yearly salary value with the uses formula 
    def get_YearlySalary(self):
        wageClass = self.get_wageLevel()
        wageLevel = self.get_wageLevel()

        salary = 48000 - 7750 + wageClass * 7000 + wageLevel * 750
        return salary

   # Display the object values
    def __str__(self):
        description = super(PermanentEmployee, self).__str__()
        description += f"Child - permanent employee\n"
        description += f"Wage Class: {self.get_wageClass()}\n" 
        description += f"Wage Level: {self.get_wageLevel()}\n"
        description += f"Yearly Salary: {self.get_YearlySalary()}\n"    

        return description