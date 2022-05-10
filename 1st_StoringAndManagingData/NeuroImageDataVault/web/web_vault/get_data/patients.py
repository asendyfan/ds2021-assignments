from .DBConnection import conn, excuteSql, getData
from os import listdir
from os.path import isfile, join
from django.templatetags.static import static

def getfile(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(123123, onlyfiles)
    return onlyfiles


def getPatientsLen(sessionid):
    sql = 'Select * from linkparticipate \
        inner join hubsession on hubsession.sessionhashkey = linkparticipate.sessionhashkey\
            where hubsession.sessionid = \'{}\''.format(sessionid)
    
    raw = excuteSql(sql)
    print(raw)
    return len(raw)

def getPatient(patientid='patient1'):
    cols = ['patientid', 'patientname', 'patientage', 'patientsex']
    sql = 'select {} from HubPatient \
        INNER JOIN SatPatient \
            ON HubPatient.PatientHashkey=SatPatient.PatientHashkey \
        where patientid = \'{}\';'.format(
            str(cols).replace('\'', '').replace('[', '').replace(']', ''),
            patientid
        )
    data = getData(sql, cols)
    item = data[0] if len(data) > 0 else {}
    types = ['oxy','deoxy','total', 'mes_wl1', 'mes_wl2']
    item['types'] = types
    return item


def getPatients(id):

    return [
        {'age':20, 'sex':'Male', 'name':'Bob', "patient_id":1},
        {'age':20, 'sex':'Male', 'name':'Alice', "patient_id":1}
    ]


def onePatientData(id):
    return {
        'patient':{
            'age':20, 'sex':'Male', 'name':'Bob', "patient_id":1
        },
        'results':[
            {'desc':'xxx plot', 'imgurl':'/static/test/Lena.png'},
            {'desc':'xxx plot', 'imgurl':'/static/test/cat.jpg'},
        ]
    }