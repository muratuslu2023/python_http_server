"""

Core management scripts.

"""

import os
import json
from ...lib.printer.printers import Printer
from ..server.host_validation import HOSTValidator

printer = Printer()


def getCurrentDIR():
    return os.path.dirname(os.path.realpath(__file__))

class RunServer():
    def __init__(self):
        self.host_validator = HOSTValidator()
    def execute(self,args):
        #check whether the server folders exist
        NO_PROBLEM = True #
        if NO_PROBLEM:
            if len(args) > 1:   #meaning that there might be a HOST:PORT -> validate them!
                second_arg = str(args[1])
                if second_arg.split(":")[0] == second_arg:
                    print(printer.INFO + printer.FAIL("Invalid HOST:PORT Pattern!"))
                    exit(-1)
                else:
                    validation = self.host_validator.validate(HOST=second_arg.split(":")[0],PORT=second_arg.split(":")[1])
                    if validation:
                        print(printer.INFO + printer.BOLD("Valid Given HOST:PORT Pattern!"))
                        print(printer.INFO + printer.BOLD("The Server is Starting..."))
                        #given_host_port = (second_arg.split(":")[0],second_arg.split(":")[1])
                    else:
                        print(printer.INFO + printer.FAIL("Invalid HOST:PORT Pattern!"))
                        exit(-1)
            else:
                validation = self.host_validator.validate(HOST=None,PORT=None)
                if validation:
                    print(printer.INFO + printer.BOLD("Valid Given .env HOST:PORT Pattern!"))
                    print(printer.INFO + printer.BOLD("The Server is Starting..."))
                else:
                    print(printer.INFO + printer.FAIL("Invalid HOST:PORT Pattern!"))
                    exit(-1)
class Manager():
    def __init__(self,args:list[str]):
        self.args = args
        self.getJSONFile()
        self.getOptionTypes()

        self.runserver = RunServer()
    
    def getJSONFile(self):
        try:
            json_location = os.path.join(getCurrentDIR(),"options.json")
            self.json_file = open(json_location,"r",encoding="utf-8")
        except FileNotFoundError as e:
            print(f"Could not find JSON file at: {json_location}")
            exit(-1)
            
    def getOptionTypes(self):
        json_object = dict(json.load(self.json_file))
        self.option_types = json_object["options"]
        self.json_file.close()

    def execute(self):
        self.stripped_args = self.args[1:]
        if self.stripped_args == []:

            print(printer.INFO + printer.BOLD("No Arguments Provided!"))
            print(printer.BOLD("Options:"))
            
            for i in self.option_types:
                print(f"\t{i}")
        else:
            if self.stripped_args[0] in self.option_types:
                """ print(self.stripped_args) """
                self.callCorresponingClass(option_type=self.stripped_args[0])
            else:
                print(printer.INFO + printer.FAIL("Invalid Option Type: ") + self.stripped_args[0])

    def callCorresponingClass(self,option_type):
        if option_type == "runserver":
            self.runserver.execute(self.stripped_args)

def getArguments(args):
    manager = Manager(args=args)
    manager.execute()
    