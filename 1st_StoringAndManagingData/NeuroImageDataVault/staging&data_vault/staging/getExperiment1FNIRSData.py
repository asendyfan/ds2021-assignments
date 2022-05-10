from code.staging.read_VMData import VMData
import os
from code.staging.exp2FnirsTools import getFilePath
import numpy as np

directory = 'data/VMData/'
# filenames = os.listdir(path)
# dataList = []
# for filename in filenames:
#     tmp = VMData(path+'/'+filename)
#     ch = tmp.CH()
#     # dataList.append(tmp)


def getExp1Data(uniqueStr):
    filenames = os.listdir(directory)
    data = np.array([]).reshape(0, 4)
    for filename in filenames:
        if uniqueStr in filename:
            print('reading', filename)
            vm = VMData(directory+filename)
            data = np.vstack((data, vm.Data(time_index=26 if uniqueStr != 'MES' else 50)))
    return data