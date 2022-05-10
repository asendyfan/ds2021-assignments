import os
from h5py import File
import numpy as np
import datetime
from code.staging.tools import getSHA256
import csv



def getExp2EEGDataHash(source):
    keys = source.split('.')
    split_index = keys[2].find('-')
    patientNumber = keys[2][:split_index]
    stimulusNumber = keys[2][split_index+1:]
    patientNumber = int(patientNumber.replace('Control', '').replace('control', ''))
    hashKey = getSHA256('exp{exp}-exp{exp}_{patient}-exp{exp}_{stimulus}'.format(exp=keys[0], patient=patientNumber, stimulus=stimulusNumber))
    return hashKey

class EEG:
    def __init__(self, filepath):
        self.source = 'Dataset2.'+filepath[5:].replace('/', '.').replace('.mat', '')
        self.file = File(filepath, 'r')

    def getSource(self):
        return self.source

    def ID(self):
        source = self.source
        keys = source.split('.')
        split_index = keys[2].find('-')
        patientNumber = keys[2][:split_index]
        stimulusNumber = keys[2][split_index + 1:]
        patientNumber = int(patientNumber.replace('Control', '').replace('control', ''))
        id = 2 * (patientNumber-1) + int(stimulusNumber)
        return 'eeg'+str(id)

    def Session(self):
        source = self.source
        keys = source.split('.')
        split_index = keys[2].find('-')
        patientNumber = keys[2][:split_index]
        stimulusNumber = keys[2][split_index + 1:]
        return stimulusNumber

    def write(self, path):
        key = list(self.file.keys())[0]
        source = self.getSource()
        hashkey = getExp2EEGDataHash(source)
        id = self.ID()
        data = self.file[key]
        tmp = '{'
        for row in data:
            tmp += '{'
            for value in row:
                tmp += str(value)+','
            tmp = tmp[:-1] + '},'
        tmp = tmp[:-1] + '}'
        path.writerow([hashkey, source, id, tmp])

    def Data(self):
        key = list(self.file.keys())[0]
        source = self.getSource()
        # hashkey = getExp2EEGDataHash(source)
        id = self.ID()
        hashkey = getSHA256(id)
        data = self.file[key]
        tmp = []
        for row in data:
            tmp.append(list(row))
        tmp = 'array'+str(tmp)
        sqldata = "('"+hashkey+"'"+','+"'"+source+"'"+','+"'"+id+"'"+','+tmp+')'
        return sqldata

    def getData(self):
        """
        path: str
        Returns: [recordDate(datetime), source (str), data (float[])]
        """
        key = list(self.file.keys())[0]
        fileValue = np.array(self.file[key])
        oneItemData = []
        source = self.getSource()
        hashKey = getExp2EEGDataHash(source)
        for v in fileValue:
            recordDate = v[0]
            oneItemData.append([hashKey, str(datetime.timedelta(recordDate)), source, v[1:]])
        return np.array(oneItemData)



def getAllEEG():
    """`
    Returns: [hash, recordDate(datetime), source (str), data (float[])][]
    """
    directory = 'data/EEG-Data/'
    filenamelist = os.listdir(directory)
    print('total file {}'.format(len(filenamelist)))
    data = np.array([]).reshape(0, 4)
    for filename in filenamelist[:2]:
        if filename == '.gitignore':
            continue
        print('open {}'.format(filename))
        eeg = EEG(directory+filename)
        item = eeg.getData()
        data = np.vstack([data, item])
        
    return np.array(data)





def main():
    # file = open('data/EEG-Data/Control001-1.mat', 'r')
    # aa = file.readlines()
    # print(aa)
    eeg = EEG('data/EEG-Data/Control001-1.mat')
    eeg.ID()
    data = eeg.getData()






