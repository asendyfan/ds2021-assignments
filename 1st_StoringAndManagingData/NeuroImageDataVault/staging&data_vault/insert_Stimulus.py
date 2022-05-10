import psycopg2
from code.staging.tools import getSHA256


def insert_Stimulus(database='project', user='postgres', password='19980806', port='5432'):
    """insert Stimulus data"""
    print("\n*************Starting populating for Stimulus*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    source = ['Dataset1.Moto', 'Dataset1.Rest', 'Dataset1.ViMo', 'Dataset1.Viso', 'Dataset2', 'Dataset2']
    id = ['sti1', 'sti2', 'sti3', 'sti4', 'sti5', 'sti6']
    hashkey = []
    for i in id:
        hashkey.append(getSHA256(i))
    level = ['Motor', 'Rest', 'VisuoMotor', 'Visual', 'NormalConversation', 'NormalConversationWithSyllables']

    for i in range(6):
        sql = "insert into staging.stimulus values ('" + hashkey[i] + "','" + source[i] + "','" + id[i] + "','" + level[i] + "');"
        cur.execute(sql)

    conn.commit()
    conn.close()
