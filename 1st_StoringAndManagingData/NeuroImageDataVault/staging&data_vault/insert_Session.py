import psycopg2
from code.staging.tools import getSHA256


def insert_Session(database='project', user='postgres', password='19980806', port='5432'):
    """insert Session data"""
    print("\n*************Starting populating for Session*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    source = ['Dataset1.Moto', 'Dataset1.Rest', 'Dataset1.ViMo', 'Dataset1.Viso', 'Dataset2_EEG.-1.mat+Dataset2_FNIRS.1raSessionDR', 'Dataset2_EEG.-2.mat+Dataset2_FNIRS.2daSessionDR']
    id = ['session1', 'session2', 'session3', 'session4', 'session5', 'session6']
    hashkey = []
    for i in id:
        hashkey.append(getSHA256(i))

    for i in range(6):
        sql = "insert into staging.session values ('" + hashkey[i] + "','" + source[i] + "','" + id[i] + "');"
        cur.execute(sql)
    conn.commit()
    conn.close()
