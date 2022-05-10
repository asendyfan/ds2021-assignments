import psycopg2
from code.staging.tools import getSHA256
import os
from code.staging.read_VMData import VMData
from code.staging.read_inf import INF


def insert_Patient(database='project', user='postgres', password='19980806', port='5432'):
    """insert LinkPatient data"""
    print("\n*************Starting populating for Patient*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    path = 'data/VMData'
    files = os.listdir(path)
    id = ''
    for file in files:
        if file == '.gitignore':
            continue
        vm = VMData(path + '/' + file)
        vm.createDict()
        if id == vm.ParticipantID():
            continue
        id = vm.ParticipantID()
        name = vm.ParticipantName()
        age = vm.ParticipantAge()
        sex = vm.ParticipantSex()
        hashkey = getSHA256(id)
        sql = "insert into staging.patient values ('" + hashkey + "','" + vm.getSource().replace('data.VMData.','')[:15] + "','" + id + "','" + name + "','" + str(age) + "','" + sex + "');"
        print(sql)
        cur.execute(sql)

    path1 = 'data/fNIRS-Data/1raSessionDR'
    subpath = os.listdir(path1)
    for path in subpath:
        if path == 'desktop.ini':
            continue
        for file in os.listdir(path1+'/'+path):
            if 'inf' in file:
                inf = INF(path1+'/'+path+'/'+file)
                id = inf.getID()
                hashkey = getSHA256(id)
                name = inf.Name()
                age = inf.Age()
                sex = inf.Gender()
                source = inf.getSource()
                sql = "insert into staging.patient values ('" + hashkey + "','" + source[:19] + "','" + id + "','" + name.lower() + "','" + str(age) + "','" + sex + "');"
                print(sql)
                cur.execute(sql)

    conn.commit()
    conn.close()
