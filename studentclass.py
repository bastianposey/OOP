from datetime import date
class Student:
    def __init__(self,id,name,dob,classification):
        self.__studentid = id
        self.__name = name
        self.__dob = dob
        self.__class = classification
        self.__age = 0
        self.__register = ''

    def get_age(self):
        return self.__age

    def get_studentid(self):
        return self.__studentid

    def get_name(self):
        return self.__name

    def get_dob(self):
       return self.__dob
        
    def get_class(self):
       return self.__class
    def get_register(self):
        return self.__register
    
    def register(self):
        if(self.__class == 'Senior'):
            self.__register = "Seniors - 11/1 thru 11/3"

        elif(self.__class == 'Junior'):
            self.__register = "Juniors - 11/4 thru 11/6"

        elif(self.__class == 'Sophomore'):
            self.__register = "Sophormores - 11/7 thre 11/9"

        elif(self.__class == 'Freshmen'):
            self.__register = "Freshmen - 11/10 thru 11/12"

        else:
            self.__register = "classification not found"
            
    def calc_age(self):
        today = date.today()
        bday = self.__dob.split('/')
        bday_year = int(bday[2])
        age = today.year - bday_year
        self.__age = age
        