import psycopg2
import os
from code.staging.read_VMData import VMData
from code.staging.readWL import WL
from code.staging.readDat import Dat


def insert_fNIRS(database='project', user='postgres', password='19980806', port='5432'):
    """insert fNIRS data"""
    print("\n*************Starting populating for fNIRS*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    VM_path = 'data/VMData'
    VM_files = os.listdir(VM_path)
    sessions = ['Moto', 'Rest', 'ViMo', 'Viso']
    hashkeys = []
    for i in range(4):
        for file in VM_files:
            if file == '.gitignore':
                continue
            vm = VMData(VM_path + '/' + file)
            vm.createDict()
            if vm.Session() == sessions[i]:
                hashkey = vm.Hash()
                if hashkey in hashkeys:
                    sql = "update staging.fnirs set "+vm.Type()+" = "+'array'+str(vm.CH())+" where fnirsdatahashkey = '"+vm.Hash()+"';"
                    #print(sql)
                    cur.execute(sql)
                    print("Successfully insert " + file)
                    conn.commit()
                else:
                    hashkeys.append(hashkey)
                    flag = vm.getSource().find('P')
                    source = vm.getSource()[:flag-5]
                    id = vm.ID()
                    data = vm.CH()
                    sqldata = "('"+hashkey+"'"+','+"'"+source+"'"+','+"'"+id+"'"+','+'array'+str(data)+');'
                    sql = "insert into staging.fnirs (fnirsdatahashkey, recordsource, fnirsdataid, deoxy) values "+sqldata
                    #print(sql)
                    cur.execute(sql)
                    print("Successfully insert " + file)
                    conn.commit()

    WL_path1 = 'data/fNIRS-Data/1raSessionDR'
    WL_path2 = 'data/fNIRS-Data/2daSessionDR'
    subpath1 = os.listdir(WL_path1)
    subpath2 = os.listdir(WL_path2)
    for path in subpath1:
         if path == 'desktop.ini':
             continue
         for file in os.listdir(WL_path1+'/'+path):
             if 'wl1' in file:
                 wl1 = WL(WL_path1+'/'+path+'/'+file)
                 sql = "insert into staging.fnirs (fnirsdatahashkey, recordsource, fnirsdataid, wavelength1) values " + wl1.sqldata() + ';'
                 #print(sql)
                 cur.execute(sql)
                 print("Successfully insert " + file)
                 # print(wl1.ID())
                 conn.commit()
             if 'wl2' in file:
                 wl2 = WL(WL_path1 + '/' + path + '/' + file)
                 sql = "update staging.fnirs set wavelength2 = arra" + wl2.sqldata().split('a')[-1][:-1] + " where fnirsdatahashkey = '" + wl2.Hash() + "';"
                 #print(sql)
                 cur.execute(sql)
                 print("Successfully insert " + file)
                 # print(wl2.ID())
                 conn.commit()
             '''if file == 'Detectors':
                 tmp = os.listdir(WL_path1+'/'+path+'/'+file)
                 tmp.remove('desktop.ini')
                 dat = Dat(WL_path1+'/'+path+'/'+file+'/'+tmp[0])
                 sql = "update staging.fnirs set hb = " + dat.Data() + " where fnirsdatahashkey = " + wl1.Hash() + ';' '''

    for path in subpath2:
        if path == 'desktop.ini':
            continue
        for file in os.listdir(WL_path2+'/'+path):
            if 'wl1' in file:
                wl1 = WL(WL_path2 + '/' + path + '/' + file)
                sql = "insert into staging.fnirs (fnirsdatahashkey, recordsource, fnirsdataid, wavelength1) values " + wl1.sqldata() + ';'
                #print(sql)
                cur.execute(sql)
                print("Successfully insert " + file)
                # print(wl1.ID())
                conn.commit()
            if 'wl2' in file:
                wl2 = WL(WL_path2 + '/' + path + '/' + file)
                sql = "update staging.fnirs set wavelength2 = arra" + wl2.sqldata().split('a')[-1][:-1] + " where fnirsdatahashkey = '" + wl2.Hash() + "';"
                #print(sql)
                cur.execute(sql)
                print("Successfully insert " + file)
                # print(wl2.ID())
                conn.commit()


    conn.close()
