class Employe:
    
    def __init__(self, lastName, firstName, personalid):
        """Initializes a new employe object with the given values and validation"""
        
        # Validate given parameter types
        if not isinstance(lastName, str):
            raise ValueError(lastName, 'has the wrong type. The given type needs to be string.')
        if not isinstance(firstName, str):
            raise ValueError(firstName, 'has the wrong type. The given type needs to be string.')
        if not isinstance(personalid, str):
            raise ValueError(personalid, 'has the wrong type. The given type needs to be string.')

        # Initialize class properties
        self.__lastName = lastName
        self.__firstName = firstName
        self.__personalid = personalid
        self.__organization = None
        self.__supervisor = None


    # get method for the organization parameter 
    def get_organization(self):
        return self.__organization

    # set method for the organization parameter 
    def set_organization(self, value):
        if not isinstance(value, str):
            raise ValueError(value, 'has the wrong type. The given type needs to be string.')        
        else:
            self.__organization = value

    # get method for the supervisor parameter 
    def get_supervisor(self):
        return self.__supervisor

    # set method for the supervisor parameter 
    def set_supervisor(self, value): 
        if not isinstance(value, str):
            raise ValueError(value, 'has the wrong type. The given type needs to be string.')        
        else:
            self.__organization = value
            
    # get method for the lastName parameter 
    def get_lastName(self):
        return self.__lastName

    # get method for the firstName parameter 
    def get_firstName(self):
        return self.__firstName

    # get method for the personalId parameter 
    def get_personalId(self):
        return self.__personalid    


    # Display the object values
    def __str__(self):
        description = "Parent - Employee:\n"
        description += f"Personal ID: {self.get_personalId()}\n"
        description += f"Firstname: {self.get_firstName()}\n"
        description += f"Lastname: {self.get_lastName()}\n"
        
        if self.get_organization() != None:
            description += f"Organization: {self.get_organization()}\n"
        if self.get_supervisor() != None:
            description += f"Supervisor: {self.get_supervisor()}\n"

        return description






