class Employe:
    
    def __init__(self, lastName, firstName, personalid):
        """Initializes a new employe object with the given values and validation"""
        
        #Validate given parameter types
        if not isinstance(lastName, str):
            raise ValueError(lastName, 'has the wrong type. The given type needs to be string.')
        if not isinstance(firstName, str):
            raise ValueError(firstName, 'has the wrong type. The given type needs to be string.')
        if not isinstance(personalid, str):
            raise ValueError(personalid, 'has the wrong type. The given type needs to be string.')

        #Initialize class properties
        self.__lastName = lastName
        self.__firstName = firstName
        self.__personalid = personalid
        self.__organization = None
        self.__supervisor = None


    #get method for the organization parameter 
    def get_organization(self):
        return self.__organization

    #set method for the organization parameter 
    def set_organization(self, value):
        self.__organization = value

    #get method for the supervisor parameter 
    def get_supervisor(self):
        return self.__supervisor

    #set method for the supervisor parameter 
    def set_supervisor(self, value):
        self.__supervisor = value   
    
    #get method for the lastName parameter 
    def get_lastName(self):
        return self.__lastName

    #get method for the firstName parameter 
    def get_firstName(self):
        return self.__firstName

    #get method for the personalId parameter 
    def get_personalId(self):
        return self.__personalid    


    def _str_(self):
        print('Lastname:', self.__lastName)
        print('Firstname:', self.__firstName)    
        print('PersonalId:', self.__personalid)    
        print('Organization:', self.get_organization())    
        print('Supervisor:', self.get_supervisor()) 
    



