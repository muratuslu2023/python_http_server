from ..os.os_operations import OSOperations
import os
import re

class HOSTValidator():
    def __init__(self):
        self.osoperations = OSOperations(__file__)
        self.currentDirectory = self.osoperations.getCurrentDirectory()
        self.rootDirectory = self.osoperations.goParentDirectory(self.currentDirectory,3)
        self.envFile = self.osoperations.getEnv()

    
    
    def validate(self,HOST,PORT):
        from dotenv import load_dotenv
        load_dotenv(self.envFile)

        ENV_HOST = str(os.getenv("SERVER_HOST"))
        ENV_PORT = int(os.getenv("SERVER_PORT"))

        #the valid HOST format is either "localhost" or "000.000.000.000"
        #the valid PORT format should be between 1024 (included) and 65535 (included)

        if PORT != None:
            p_check = self.PORTCheck(PORT=PORT)
        elif PORT == None:
            p_check =  self.PORTCheck(PORT=ENV_PORT)
        if HOST != None:
            h_check =  self.HOSTCheck(HOST=HOST)
        elif HOST == None:
            h_check =  self.HOSTCheck(HOST=ENV_HOST)
        
        if h_check == True and p_check == True:
            return True
        else:
            return False
        
    
    def PORTCheck(self,PORT:int):
        if PORT == None:
            return False
        else:
            try:
                PORT = int(PORT)
            except ValueError:
                return False
            if PORT < 1024 or PORT > 65535:
                return False
            else:
                return True
    def HOSTCheck(self,HOST:str):
        if HOST == None:
            return False
        else:
            if HOST == "localhost":
                return True
            else:
                ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
                hostname_pattern = r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])*$'
                if re.match(hostname_pattern, HOST):
                    return False
                elif re.match(ipv4_pattern, HOST):
                    return True
                else:
                    return False
        
