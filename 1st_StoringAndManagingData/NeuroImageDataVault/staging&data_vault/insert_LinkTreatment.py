import psycopg2
from code.staging.tools import getSHA256


def insert_LinkTreatment(database='project', user='postgres', password='19980806', port='5432'):
        """insert LinkTreatment data"""
        print("\n*************Starting populating for LinkTreatment*************\n")
        conn = psycopg2.connect(database=database, user=user, password=password, port=port)
        print("Connect database successfully!")
        cur = conn.cursor()

        source = ['Dataset1', 'Dataset1', 'Dataset1', 'Dataset1','Dataset2','Dataset2']
        id1 = ['session1', 'session2', 'session3', 'session4', 'session5', 'session6']
        id2 = ['sti1', 'sti2', 'sti3', 'sti4', 'sti5', 'sti6']

        for i in range(6):
                id = id1[i] + '_' + id2[i]
                hashkey1 = getSHA256(id1[i])
                hashkey2 = getSHA256(id2[i])
                hashkey = getSHA256(id)
                sql = "insert into staging.linktreatment values ('" + hashkey + "','" + source[i] + "','" + hashkey1 + "','" + hashkey2 + "');"
                cur.execute(sql)
                print("%s: %s <-> %s" % (id1[i], 'session5', id2[i]))

        conn.commit()
        conn.close()