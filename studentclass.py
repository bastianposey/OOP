class student:
    def __init__(self):
        self.__studentid = 0
        self.__name = ""
        self.__dob = ""
        self.__class = ''

    def get_studentid(self,id):
        self.__studentid = id

    def get_name(self,nam):
        self.__name = nam

    def get_dob(self,dob):
        self.__dob = dob
        
    def get_class(self,clas):
        self.__class = clas