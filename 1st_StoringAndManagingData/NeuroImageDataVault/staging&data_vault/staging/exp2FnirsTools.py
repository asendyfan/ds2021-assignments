from code.staging.tools import getSHA256
import datetime
import numpy as np
import pandas as pd
import json
import os


def getExp2FnirsDataHash(source):
    keys = source.split('.')
    patientNumber, stimulusNumber = keys[3].split('-')
    patientNumber = int(patientNumber.replace('Autism', ''))
    # print(keys[0], patientNumber, stimulusNumber)
    hashKey = getSHA256('exp{exp}-exp{exp}_{patient}-exp{exp}_{stimulus}'.format(exp=keys[0], patient=patientNumber, stimulus=stimulusNumber))
    return hashKey


def getExp2FnirsStartingTime(meta):
    filename = meta['GeneralInfo']['FileName']
    date = filename[filename.find('-')+1:filename.rfind('_')]
    time = meta['GeneralInfo']['Time']
    time = time[:time.rfind('.')]
    theTime = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M:%S')
    return theTime


def getFilePath(uniqueStr, currentDirectory):
    fileNames = os.listdir(currentDirectory)
    return currentDirectory + '/' + list(filter(lambda filename: uniqueStr in filename, fileNames))[0]

def storingDataToJson(data, fileName, direcotry = 'data/staging/'):
    transData = data
    print(type(transData), type(transData) is np.ndarray)
    if type(data) is np.ndarray:
        transData = transData.tolist()
    print('writing the file: ', direcotry+fileName+'.json')
    storingPath = direcotry + fileName
    file = open(storingPath+'.json', 'w+')
    # file.write()
    json.dump(transData, file)
    print('writing success')


def storingDataToCSV(data, fileName, directory='data/staging/'):
    storingPath = directory + fileName
    print('writing the file: ', storingPath+'.csv')
    header = ['hashKey', 'recordDate', 'source', 'data']
    pd.DataFrame(data, columns=header).to_csv(storingPath+'.csv', index=False)
    # np.savetxt(storingPath+'.csv', data, delimiter=',', fmt='%s')
    print('writing success')