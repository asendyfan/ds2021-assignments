import os

class INF:
    def __init__(self, filepath):
        self.name = filepath[-23:]
        self.data = open(filepath, 'r', encoding='ISO-8859-1')
        self.source = 'Dataset2.'+filepath[5:].replace('/', '.').replace('.inf', '')

    def getID(self):
        # id = self.Name().replace('Control','').replace('control', '').split('-')[0]
        keys = self.source.split('.')
        patientNumber, stimulusNumber = keys[3].split('-')
        patientNumber = int(patientNumber.replace('Autism', '')) + 10
        return 'patient'+str(patientNumber)

    def getSource(self):
        return self.source

    def Name(self):
        for row in self.data:
            row = row.strip().split('=')
            if row[0] == 'Name':
                return row[1].split('-')[0][1:]
                break

    def Age(self):
        for row in self.data:
            row = row.strip().split('=')
            if row[0] == 'Age':
                return row[1]
                break

    def Gender(self):
        for row in self.data:
            row = row.strip().split('=')
            if row[0] == 'Gender':
                return 'Male' if row[1].replace('"', '') == "M" else "Female"
                break


if __name__ == "__main__":
    path1 = 'data/fNIRS-Data/1raSessionDR'
    path2 = 'data/fNIRS-Data/2daSessionDR'

    filepaths = []
    subpath1 = os.listdir(path1)[:-1]
    subpath2 = os.listdir(path2)[:-2]
    for subpath in subpath1:
        tmp = os.listdir(path1+'/'+subpath)
        for file in tmp:
            if '.inf' in file:
                filepaths.append(path1+'/'+subpath+'/'+file)
    for subpath in subpath2:
        tmp = os.listdir(path2+'/'+subpath)
        for file in tmp:
            if '.inf' in file:
                filepaths.append(path2+'/'+subpath+'/'+file)

    infs = []
    for filepath in filepaths:
        inf = INF(filepath)
        infs.append(inf)
    
    # return info
