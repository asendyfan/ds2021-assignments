import os
import numpy as np
from code.staging.tools import getSHA256

def getExp1FnirsDataHash(source):
    keys = source.split('.')
    # print(111,keys)
    vs = keys[3].split('_')
    patientNumber = int(vs[0][2:])
    stimulusNumber = vs[1]
    # print(source, keys[0], patientNumber, stimulusNumber)
    hashKey = getSHA256('exp{exp}-exp{exp}_{patient}-exp{exp}_{stimulus}'.format(exp=keys[0], patient=patientNumber, stimulus=stimulusNumber))
    #print('exp{exp}-exp{exp}_{patient}-exp{exp}_{stimulus}'.format(exp=keys[0], patient=patientNumber, stimulus=stimulusNumber))
    return hashKey


class VMData:
    def __init__(self, filepath):
        self.name = filepath[12:]
        self.source = 'Dataset1.'+filepath.replace('/', '.').replace('.csv', '')
        self.data = open(filepath, 'r')
        self.dict = {}

    def getSource(self):
        return self.source

    def ID(self):
        source = self.source
        keys = source.split('.')
        vs = keys[3].split('_')
        patientNumber = int(vs[0][2:])
        stimulusNumber = vs[1]
        stimulus = 'MotoRestViMoViso'
        id = int(4 * (patientNumber-1) + stimulus.find(self.Session())/4)+1
        return 'fNIRS' + str(id)

    def Hash(self):
        hashkey = getSHA256(self.ID())
        return hashkey

    def Session(self):
        source = self.source
        keys = source.split('.')
        vs = keys[3].split('_')
        return vs[1]

    def Type(self):
        source = self.source
        keys = source.split('.')
        vs = keys[3].split('_')
        if vs[2] == 'MES':
            return 'mes'
        else:
            return vs[-1].lower()

    def Filename(self):
        return self.name

    def createDict(self):
        for row in self.data:
            row = row.strip().split(',')
            self.dict[row[0]] = row[1:]
            if 'Data' in row[0]:
                break

    def ParticipantID(self):
        return 'patient' + str(int((self.dict['ID'][0].split('_')[0])[4:]))

    def ParticipantName(self):
        return self.dict['Name'][0]

    def ParticipantAge(self):
        return int(self.dict['Age'][0][1:-1])

    def ParticipantSex(self):
        return self.dict['Sex'][0]

    def Date(self):
        # print(self.dict)
        return self.dict['Date'][0]

    def WaveLength(self):
        return self.dict['Wave Length']

    def CH(self):
        ch = []
        for row in self.data:
            row = row.strip().split(',')
            ch.append(row[1:])
        return ch


    def Data(self, time_index=26):
        ch = []
        ch_index = -1
        date = ''
        for i, row in enumerate(self.data):
            if 'Date,' in row:
                date = row.strip().split(',')[1].replace('/', '-').split(' ')[0]
            if 'Data' in row:
                ch_index = i + 2
            if (ch_index>0) and (i>=ch_index):
                row = row.strip().split(',')
                # hash, recorddate, source, data
                source = self.getSource()
                hashkey = getExp1FnirsDataHash(source)
                ch.append([hashkey, date+' '+row[time_index], source, [float(v) for v in [*row[1:time_index], *row[time_index+1:]]]])
        return ch



# if __name__ == "__main__": 
#     path = 'data/VMData'
#     filenames = os.listdir(path)
#     dataList = []
#     for filename in filenames:
#         tmp = VMData(path+'/'+filename)
#         tmp.createDict()
#         dataList.append(tmp)
