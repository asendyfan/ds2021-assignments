import psycopg2
from code.staging.tools import getSHA256
import os
from code.staging.read_VMData import VMData
from code.staging.read_inf import INF


def insert_LinkParticipate(database='project', user='postgres', password='19980806', port='5432'):
    """insert LinkParticipate data"""
    print("\n*************Starting populating for LinkParticipate*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    id1 = ['session1', 'session2', 'session3', 'session4', 'session5', 'session6']
    # hashkey1 = getSHA256(id1)

    path = 'data/VMData'
    files = os.listdir(path)
    id2 = ''
    for i, stimulus in enumerate(['Moto', 'Rest', 'ViMo', 'Viso']):
        for file in files:
            if file == '.gitignore':
                continue
            vm = VMData(path+'/'+file)
            if vm.Session() == stimulus:
                vm.createDict()
                hashkey1 = getSHA256('session'+str(i+1))
                if id2 == vm.ParticipantID():
                    continue
                id2 = vm.ParticipantID()
                hashkey2 = getSHA256(id2)
                id = 'session' + str(i+1) + '_' + id2
                hashkey = getSHA256(id)
                sql = "insert into staging.linkparticipate values ('" + hashkey + "','" + vm.getSource().replace('data.VMData.','') + "','" + hashkey1 + "','" + hashkey2 + "');"
                # print(sql)
                print("%s: %s <-> %s" % (id, 'session'+str(i+1), id2))
                cur.execute(sql)

    path1 = 'data/fNIRS-Data/1raSessionDR'
    subpath = os.listdir(path1)
    for path in subpath:
        if path == 'desktop.ini':
            continue
        for file in os.listdir(path1+'/'+path):
            if 'inf' in file:
                inf = INF(path1+'/'+path+'/'+file)
                hashkey1 = getSHA256('session5')
                id2 = inf.getID()
                hashkey2 = getSHA256(id2)
                id = 'session5_' + id2
                hashkey = getSHA256(id)
                sql = "insert into staging.linkparticipate values ('" + hashkey + "','" + inf.getSource() + "','" + hashkey1 + "','" + hashkey2 + "');"
                # print(sql)
                print("%s: %s <-> %s" % (id, 'session5', id2))
                cur.execute(sql)

    path2 = 'data/fNIRS-Data/2daSessionDR'
    subpath = os.listdir(path2)
    for path in subpath:
        if path == 'desktop.ini':
            continue
        for file in os.listdir(path2+'/'+path):
            if 'inf' in file:
                inf = INF(path2+'/'+path+'/'+file)
                hashkey1 = getSHA256('session6')
                id2 = inf.getID()
                hashkey2 = getSHA256(id2)
                id = 'session6_' + id2
                hashkey = getSHA256(id)
                sql = "insert into staging.linkparticipate values ('" + hashkey + "','" + inf.getSource() + "','" + hashkey1 + "','" + hashkey2 + "');"
                # print(sql)
                print("%s: %s <-> %s" % (id, 'session6', id2))
                cur.execute(sql)

    conn.commit()
    conn.close()
