from ..colors.color import Colors

class Printer():
    def __init__(self):
        self.colors = Colors()
        self.INFO = f"{self.colors.OKGREEN}[INFO]{self.colors.ENDC} "
    
    def BOLD(self,text,*args):
        return f"{self.colors.BOLD}{text}{self.colors.ENDC}"
    
    def UNDERLINE(self,text,*args):
        return f"{self.colors.UNDERLINE}{text}{self.colors.ENDC}"
    
    def OKGREEN(self,text,*args):
        return f"{self.colors.OKGREEN}{text}{self.colors.ENDC}"
    
    def WARNING(self,text,*args):
        return f"{self.colors.WARNING}{text}{self.colors.ENDC}"
    def FAIL(self,text,*args):
        return f"{self.colors.FAIL}{text}{self.colors.ENDC}"
    