import psycopg2
from code.staging.tools import getSHA256
import os
from code.staging.read_inf import INF
from code.staging.readEEG import EEG


def insert_LinkEEGMeasure(database='project', user='postgres', password='19980806', port='5432'):
    """insert LinkEEGMeasure data"""
    print("\n*************Starting populating for LinkEEGMeasure*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    path = 'data/EEG-Data'
    files = os.listdir(path)
    for file in files:
        if file == '.gitignore':
            continue
        eeg = EEG(path+'/'+file)
        if eeg.Session() == '1':
            source = eeg.getSource()
            hashkey1 = getSHA256('session5')
            id2 = eeg.ID()
            hashkey2 = getSHA256(id2)
            id = 'session5_' + id2
            hashkey = getSHA256(id)
            sql = "insert into staging.linkeegmeasure values ('" + hashkey + "','" + source + "','" + hashkey1 + "','" + hashkey2 + "');"
            #print(sql)
            cur.execute(sql)
            print('successfully inserted', file)
            print("%s: %s <-> %s" % (id, 'session5', id2))
    for file in files:
        if file == '.gitignore':
            continue
        eeg = EEG(path+'/'+file)
        if eeg.Session() == '2':
            source = eeg.getSource()
            hashkey1 = getSHA256('session6')
            id2 = eeg.ID()
            hashkey2 = getSHA256(id2)
            id = 'session6_' + id2
            hashkey = getSHA256(id)
            sql = "insert into staging.linkeegmeasure values ('" + hashkey + "','" + source + "','" + hashkey1 + "','" + hashkey2 + "');"
            #print(sql)
            cur.execute(sql)
            print('successfully inserted', file)
            print("%s: %s <-> %s" % (id, 'session6', id2))

    conn.commit()
    conn.close()
