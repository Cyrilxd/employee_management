from employe import Employe
from permanentEmploye import PermanentEmployee
from hourlyWageEmploye import HourlywageEmploye

def main():

    #Create permanent Employe Object
    #Lastname: Bärbaum, Firstname: Anita, Organization: Sales, PersonalId: 78100,  Wageclass: 20, Wagelevel: 20.
    permanenEmployeAnita = PermanentEmployee('Bärbaum', 'Anita', '78100', 20, 20)
    #set Organization
    permanenEmployeAnita.set_organization('sales')


    #Create permanent Employe Object
    #Lastname: Christensen, Firstname: Bernd, Organization: Sales, PersonalId: 88335,  Wageclass: 15, Wagelevel: 10.
    permanenEmployeBernd = PermanentEmployee('Christensen', 'Bernd', '88335', 15, 10)
    #set Organization
    permanenEmployeBernd.set_organization('sales')

    #Create hourlywage employe Object
    #Lastname: Dietbold, Firstname: Clara, Organization: Marketing, PersonalId: 91565, Hourlywage: 60
    hourlyWageEmployeClara = HourlywageEmploye('Dietbold', 'Clara', '91565', 60)
    #set Organization
    hourlyWageEmployeClara.set_organization('Marketing')

    permanenEmployeBernd.set_supervisor(permanenEmployeAnita.get_lastName() + ' ' + permanenEmployeAnita.get_firstName())

    hourlyWageEmployeClara.set_organization('Sales')

    hourlyWageEmployeClara.set_supervisor(permanenEmployeBernd.get_lastName() +' ' + permanenEmployeBernd.get_firstName())

    try: 
        permanenEmployeAnita.increaseWageLevel()
    except: 
        print(permanenEmployeAnita.get_firstName(), permanenEmployeAnita.get_lastName(), 'Wagelevel could not been updated as it reached its maximum: ', permanenEmployeAnita.get_wageLevel())

    try: 
        permanenEmployeBernd.increaseWageClass()
    except: 
        print(permanenEmployeBernd.get_firstName(), permanenEmployeBernd.get_lastName(), 'Wageclass could not been updated as it reached its maximum: ', permanenEmployeBernd.get_wageClass())
    
    print(permanenEmployeAnita)
    print('----------------------------------------')
    print(permanenEmployeBernd)
    print('----------------------------------------')
    print(hourlyWageEmployeClara)



if __name__ == "__main__":
    main()

   

    

