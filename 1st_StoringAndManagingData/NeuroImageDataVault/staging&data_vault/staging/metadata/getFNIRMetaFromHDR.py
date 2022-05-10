
def getFNIRMetaFromHDR(path:str):
    inputF = open(path, 'r', encoding='ISO-8859-1')
    rawLines = inputF.readlines()
    metaData = {}
    currentSessionName = None
    for rawLine in rawLines:
        line = rawLine[:-1]
        if line == '':
            continue
        elif line[0] == '[':
            currentSessionName = line[1:line.find(']')]
            metaData[currentSessionName] = {}
        else:
            splitIndex = line.find('=')
            key = line[0:splitIndex]
            value = line[(splitIndex+1):].replace("\"",'')
            metaData[currentSessionName][key] = value
    return metaData

if __name__ == "__main__":
    print(getFNIRMetaFromHDR('data/fNIRS-Data/1raSessionDR/Autism0013-1/NIRS-2019-10-23_003.hdr'))