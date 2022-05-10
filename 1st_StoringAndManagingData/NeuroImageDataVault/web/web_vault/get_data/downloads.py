from .DBConnection import conn, getData, excuteSql
import pandas as pd
import zipfile

from zipfile import ZipFile
import zipfile as zf

def getMesData(sessionid, stimulusid):
    sql = "select fnirsdataid, mes, wavelength1, wavelength2 from \
        (select * from satmesdata\
        left join hubfnirsdata on satmesdata.fnirsdatahashkey = hubfnirsdata.fnirsdatahashkey\
        left join linkfnirsmeasure on hubfnirsdata.fnirsdatahashkey = linkfnirsmeasure.fnirsdatahashkey\
        left join hubsession on hubsession.sessionhashkey = linkfnirsmeasure.sessionhashkey\
        left join linktreatment on hubsession.sessionhashkey = linktreatment.sessionhashkey\
        left join hubstimulus on linktreatment.stimulushashkey = hubstimulus.stimulushashkey\
    where sessionid = '{}' and stimulusid = '{}') as data;".format(sessionid, stimulusid)
    mesdata = excuteSql(sql)
    return mesdata

def getHbaData(sessionid, stimulusid):
    sql = "select fnirsdataid,oxy, deoxy, total, hb from\
        (select * from sathbadata\
        left join hubfnirsdata on sathbadata.fnirsdatahashkey = hubfnirsdata.fnirsdatahashkey\
        left join linkfnirsmeasure on hubfnirsdata.fnirsdatahashkey = linkfnirsmeasure.fnirsdatahashkey\
        left join hubsession on hubsession.sessionhashkey = linkfnirsmeasure.sessionhashkey\
        left join linktreatment on hubsession.sessionhashkey = linktreatment.sessionhashkey\
        left join hubstimulus on linktreatment.stimulushashkey = hubstimulus.stimulushashkey\
        where sessionid = '{}' and stimulusid = '{}') as data;".format(sessionid, stimulusid)
    hbadata = excuteSql(sql)
    return hbadata
    
def downloadData(sessionid, stimulusid):
    mesdata = getMesData(sessionid, stimulusid)
    hbadata = getHbaData(sessionid, stimulusid)
    mesdata = pd.DataFrame(mesdata)
    hbadata = pd.DataFrame(hbadata)
    mesdata.to_csv('web_vault/get_data/download_temp/mes_data.csv')
    hbadata.to_csv('web_vault/get_data/download_temp/hba_data.csv')
    zipfile = ZipFile('web_vault/get_data/download_temp/{}_{}.zip'.format(sessionid, stimulusid), 'w')
    zipfile.write('web_vault/get_data/download_temp/mes_data.csv', compress_type= zf.zlib.DEFLATED)
    zipfile.write('web_vault/get_data/download_temp/hba_data.csv', compress_type= zf.zlib.DEFLATED)
    zipfile.close()
    return zipfile
