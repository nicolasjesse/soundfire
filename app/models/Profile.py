class Profile:
    def __init__(self, code, name, email, password, picture):
        self.__code = code
        self.__name = name
        self.__email = email
        self.__password = password
        self.__picture = picture

    def __str__(self):
        return  ("Code: %s Name: %s, Email: %s, Password: %s"  % (self.__code, self.__name,  self.__email, self.__password))

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def picture(self):
        return self.__picture

    @code.setter
    def code(self, new_code):
        self.__code = new_code

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @picture.setter
    def picture(self, new_picture):
        self.__picture = new_picture
