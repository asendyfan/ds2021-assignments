import psycopg2
import os
from code.staging.readEEG import EEG

def insert_EEG(database='project', user='postgre', password='19980806', port='5432'):
    """insert eeg data"""
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")

    cur = conn.cursor()

    EEG_path = 'data/EEG-Data'
    EEG_files = os.listdir(EEG_path)

    # session 5
    for file in EEG_files:
        if file == '.gitignore':
            continue
        if file[-5] == '1':
            eeg = EEG(EEG_path+'/'+file)
            print('inserting', file)
            sql = "insert into staging.eeg (hashkey, recordsource, eegdataid, eegdata) VALUES " + eeg.Data() + ';'
            #print(sql)
            cur.execute(sql)
            print(eeg.ID())
            conn.commit()

    # session 6
    for file in EEG_files:
        if file == '.gitignore':
            continue
        if file[-5] == '2':
            eeg = EEG(EEG_path+'/'+file)
            print('inserting', file)
            sql = "insert into staging.eeg (hashkey, recordsource, eegdataid, eegdata) VALUES " + eeg.Data() + ';'
            #print(sql)
            cur.execute(sql)
            print(eeg.ID())
            conn.commit()

    conn.close()
