import psycopg2
from code.staging.tools import getSHA256
import os
from code.staging.read_VMData import VMData
from code.staging.readWL import WL


def insert_LinkfNIRSMeasure(database='project', user='postgres', password='19980806', port='5432'):
    """insert LinkfNIRSMeasure data"""
    print("\n*************Starting populating for LinkfNIRSMeasure*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    path = 'data/VMData'
    files = os.listdir(path)
    id2 = ''
    for i, stimulus in enumerate(['Moto', 'Rest', 'ViMo', 'Viso']):
        for file in files:
            if file == '.gitignore':
                continue
            vm = VMData(path+'/'+file)
            if vm.Session() == stimulus:
                hashkey1 = getSHA256('session'+str(i+1))
                if id2 == vm.ID():
                    continue
                id2 = vm.ID()
                hashkey2 = getSHA256(id2)
                id = 'session' + str(i+1) + '_' + id2
                hashkey = getSHA256(id)
                sql = "insert into staging.linkfnirsmeasure values ('" + hashkey + "','" + vm.getSource().replace('data.VMData.','') + "','" + hashkey1 + "','" + hashkey2 + "');"
                # print(sql)
                cur.execute(sql)
                print("successfuly inserted" + file)
                print("   %s: %s <-> %s" % (id, 'session'+str(i+1), id2))

    path1 = 'data/fNIRS-Data/1raSessionDR'
    subpath = os.listdir(path1)
    for path in subpath:
        if path == 'desktop.ini':
            continue
        for file in os.listdir(path1+'/'+path):
            if 'wl' in file:
                wl = WL(path1+'/'+path+'/'+file)
                hashkey1 = getSHA256('session5')
                id2 = wl.ID()
                hashkey2 = getSHA256(id2)
                id = 'session5_' + id2
                hashkey = getSHA256(id)
                sql = "insert into staging.linkfnirsmeasure values ('" + hashkey + "','" + wl.getSource() + "','" + hashkey1 + "','" + hashkey2 + "');"
                # print(sql)
                cur.execute(sql)
                print("successfuly inserted" + file)
                print("   %s: %s <-> %s" % (id, 'session5', id2))
                break

    path2 = 'data/fNIRS-Data/2daSessionDR'
    subpath = os.listdir(path2)
    for path in subpath:
        if path == 'desktop.ini':
            continue
        for file in os.listdir(path2+'/'+path):
            if 'wl' in file:
                wl = WL(path2+'/'+path+'/'+file)
                hashkey1 = getSHA256('session6')
                id2 = wl.ID()
                hashkey2 = getSHA256(id2)
                id = 'session6_' + id2
                hashkey = getSHA256(id)
                sql = "insert into staging.linkfnirsmeasure values ('" + hashkey + "','" + wl.getSource() + "','" + hashkey1 + "','" + hashkey2 + "');"
                # print(sql)
                cur.execute(sql)
                print("successfuly inserted" + file)
                print("   %s: %s <-> %s" % (id, 'session6', id2))
                break

    conn.commit()
    conn.close()
