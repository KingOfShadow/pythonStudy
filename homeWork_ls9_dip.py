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


class manager:
    def __init__(self, printer, scaner, mfp):
        self.printer = printer
        self.scaner = scaner
        self.mfp = mfp
    def pr(self):
        return self.printer.print()
    def sc(self):
        return self.scaner.scan()
    def cp(self):
        return self.mfp.copinc()

pr_1 = printer()
sc_1 = scaner()
cp_1 = mfp()
man = manager(printer(), scaner(), mfp())
man.cp()