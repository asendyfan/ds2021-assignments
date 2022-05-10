from code.staging.metadata.getFNIRMetaFromHDR import getFNIRMetaFromHDR
from code.staging.exp2FnirsTools import getExp2FnirsDataHash, getExp2FnirsStartingTime, getFilePath
import datetime

class Dat:
    def __init__(self, path):
        file = open(path, 'r')
        self.source = '2.'+path[5:].replace('/', '.').replace('.dat', '')
        self.file = file.readlines()
    
        directory = path[:path.rfind('/')+1]
        self.meta = getFNIRMetaFromHDR(getFilePath('.hdr', directory))
    
    def getSource(self):
        return self.getSource()
    
    def getData(self):
        data = []
        hashKey = getExp2FnirsDataHash(self.source)
        theTime = getExp2FnirsStartingTime(self.meta)
        # print(self.file)
        for index, item in enumerate(self.file):
            data.append([
                hashKey, 
                str(theTime + datetime.timedelta(seconds = (1/5.2)*index)), 
                self.source, 
                [float(v) for v in item[:-1].split()]
            ])
        # print(data[3])
        return data

if __name__ == "__main__":
    dat = Dat('data/fNIRS-Data/1raSessionDR/Autism0001-1/NIRS-2019-10-10_001.dat')
    print(dat.getData()[3])
