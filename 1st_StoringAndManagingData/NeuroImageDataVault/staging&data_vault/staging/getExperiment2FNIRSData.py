import numpy as np
import os
from code.staging.readWL import WL
from code.staging.readDat import Dat
from code.staging.tools import getSHA256
from code.staging.exp2FnirsTools import getFilePath, storingDataToCSV

def getExp2FnirsAllData():
    direcotry = 'data/fNIRS-Data'
    sessionsDir = os.listdir(direcotry)


    wl1data = np.array([]).reshape(0, 4)
    wl2data = np.array([]).reshape(0, 4)
    datData = np.array([]).reshape(0, 4)


    for session in sessionsDir:
        if session in ['.DS_Store', '.gitignore']:
            continue
        patients = os.listdir(direcotry + '/' + session)
        for patient in patients:
            if patient in ['.DS_Store', 'desktop.ini', 'NIRS-2019-10-10_005.nirs']:
                continue
            currentDirectory = direcotry+'/'+session + '/' + patient
            
            print('current direcotry: {}'.format(currentDirectory))
            
            # read wl file
            wl1FilePath = getFilePath('wl1', currentDirectory)
            wl2FilePath = getFilePath('wl2', currentDirectory)
            wl1 = WL(wl1FilePath)
            wl2 = WL(wl2FilePath)
            wl1data = np.vstack((wl1data, wl1.getData()))
            wl2data= np.vstack((wl2data, wl2.getData()))

            # read dat file
            datFilePath = getFilePath('dat', currentDirectory)
            dat = Dat(datFilePath)
            datData = np.vstack((datData, dat.getData()))

    return wl1data, wl2data, datData


if __name__ == "__main__":
    pass
    # wl1, wl2 = getAllData()
    # print(wl1.shape, wl1[:, 1])

    # file = open('data/staging/1.json', 'w+')
    # file.write('{}')

    # wl1, wl2, dat = getExp2FnirsAllData()