from employe import Employe

class HourlywageEmploye(Employe):

    def __init__(self, lastName, firstName, personalid, hourlySalary):
        """Initizlizes a new class of a permanent employe."""
         #Validate given parameter types
        if not isinstance(hourlySalary, int):
            raise ValueError(hourlySalary, 'has the wrong type. The given type needs to be int.')
       
        #Initialize Parent Compoenent
        super().__init__(lastName, firstName, personalid)
        
        #Initialize class property
        self.__hourlySalary = hourlySalary

    #get method for the hourlySalary parameter 
    def get_hourlySalary(self):
        return self.__hourlySalary

    #set method for the hourlySalary parameter 
    def set___hourlySalary(self, value):
        self.__hourlySalary = value

    # Display the object values
    def __str__(self):
        description = super(HourlywageEmploye, self).__str__()
        description += f"Child - hourly wage employee:\n"
        
        description += f"Hourly Salary: {self.get_hourlySalary()}\n"  

        return description
    


  

        