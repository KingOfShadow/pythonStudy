class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


    def update_name(self, name):
        self.name = name

    def update_email(self, email):
        self.email = email

    def del_usr(self):
        del self.__dict__


user_1 = User('Mike', 'mail@post.com')

print(user_1.__dict__)
user_1.update_name('Tom')
print('-------------------')
print(user_1.__dict__)

user_1.del_usr()
print('-------------------')
print(user_1.__dict__)