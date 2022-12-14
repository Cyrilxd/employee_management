class Person:
    
    def __init__(self, name, firstname, personalid):
        self.__name = name
        self.__firstname = firstname
        self.__personalid = personalid



    def get_organization(self):
        return self.__organization

    def set_organization(self, value):
        self.__organization = value

    def get_supervisor(self):
        return self.__supervisor

    def set_supervisor(self, value):
        self.__supervisor = value   


    def print(self):
        print(self.__name)
        print(self.__firstname)    
        print(self.__personalid)    
        print(self.get_organization())    
        print(self.get_supervisor()) 


