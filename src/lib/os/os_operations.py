import os

class OSOperations():
    def __init__(self,file):
        self.file = file

    def getCurrentDirectory(self):
        return os.path.dirname(os.path.realpath(self.file))
    def getRootDirectory(self):
        pass
    def getEnv(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        root = self.goParentDirectory(cur_dir,3)
        return os.path.join(root,".env")
    def goParentDirectory(self,base_dir,n_times:int):
        directory = base_dir

        for i in range(n_times):
            os.path.dirname(directory)
            directory = os.path.dirname(directory)
        return directory