import os
import numpy as np
import datetime
from code.staging.tools import getSHA256


from code.staging.metadata.getFNIRMetaFromHDR import getFNIRMetaFromHDR

from code.staging.exp2FnirsTools import getExp2FnirsDataHash, getExp2FnirsStartingTime, getFilePath
class WL:
    def __init__(self, path:str):
        self.source = 'Dataset2.'+path[5:].replace('/','.').replace('wl1','').replace('wl2','')
        file = open(path, 'r')
        self.file = file.readlines()
        directory = path[:path.rfind('/')+1]
        self.meta = getFNIRMetaFromHDR(getFilePath('.hdr', directory))

    def getSource(self):
        return self.source

    def Hash(self):
        # source = self.source
        # hashkey = getExp2FnirsDataHash(source)
        hashkey = getSHA256(self.ID())
        return hashkey

    def ID(self):
        source = self.source
        keys = source.split('.')
        patientNumber, stimulusNumber = keys[3].split('-')
        patientNumber = int(patientNumber.replace('Autism', ''))
        session = int(keys[2][0])
        id = 40 + patientNumber+43*(session-1)
        return 'fNIRS'+str(id)

    def sqldata(self):
        # hashkey = self.Hash()
        source = self.source
        id = self.ID()
        hashkey = getSHA256(id)
        data = []
        for row in self.file:
            tmp = row.strip().split()
            for i in range(len(tmp)):
                tmp[i] = float(tmp[i])
            data.append(tmp)
        data = 'array'+str(data)
        sqldata = "('"+hashkey+"'"+','+"'"+source+"'"+','+"'"+id+"'"+','+data+')'
        return sqldata

    def getData(self):
        data = []
        source = self.getSource()
        hashKey = getExp2FnirsDataHash(source)
        startTime = getExp2FnirsStartingTime(self.meta)

        for index, item in enumerate(self.file):
            data.append([hashKey, str(startTime + datetime.timedelta(seconds = (1/5.2)*index)), source, [float(v) for v in item[:-1].split()]])
        return data
        

if __name__ == "__main__":
    direcotry = 'data/fNIRS-Data/1raSessionDR/Autism0001-1'
    wl = WL(direcotry+'/NIRS-2019-10-10_001.wl1')
   
    print( wl.getData()[:2])
    # wl1, wl2 = getAllData()
    # print(wl1.shape, wl1[:, 1])

