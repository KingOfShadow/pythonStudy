from abc import ABC, abstractmethod

# NetWork Printer

class net_print(ABC):
    @abstractmethod
    def print(self):
        self
class net_scan(ABC):
    @abstractmethod
    def scan(self):
        pass

class net_copier(ABC):

    @abstractmethod
    def copinc(self):
        pass
# пристрої

class printer(net_print):
    def print(self):
        print('Друкуємо')

class scaner(net_scan):
    def scan(self):
        print('Скануємо')

class mfp(net_print, net_scan, net_copier):

    def print(self):
        print('Друкуємо')

    def scan(self):
        print('Скануємо')

    def copinc(self):
        print('Скануємо')
        print('Друкуємо')
p1 = printer()
s1 = scaner()
multik = mfp()

multik.copinc()
p1.print()
s1.scan()