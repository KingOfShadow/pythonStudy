class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        print(self.__name)

    def set_name(self, new_name):
        self.__name = new_name
        print(self.__name)

    def get_email(self):
        print( self.__email)

    def set_email(self, new_mail):
        self.__email = new_mail
        print(self.__email)

    def get_pass(self):
        print(self.__password)

    def set_pass(self, new_pass):
        self.__password = new_pass
        print(self.__password)


User_1 = User("Mike", "mymail@mail.com", "password123")
User_1.get_name()
User_1.set_name('Tom')
User_1.get_email()
User_1.set_email('loss@gmail.com')
User_1.get_pass()
User_1.set_pass('admin123')