class Genre:
    def __init__(self, code, description):
        self.__code = code
        self.__description = description
        
    @property
    def code(self):
        return self.__code
    
    @property
    def description(self):
        return self.__description

    @code.setter
    def code(self, new_code):
        self.__code = new_code

    @description.setter
    def description(self, new_description):
        self.__description = new_description
