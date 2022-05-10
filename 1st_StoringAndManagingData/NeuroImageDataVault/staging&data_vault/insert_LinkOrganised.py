import psycopg2
from code.staging.tools import getSHA256


def insert_LinkOrganised(database='project', user='postgres', password='19980806', port='5432'):
    """insert LinkOrganised data"""
    print("\n*************Starting populating for LinkOrganised*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    source = ['Dataset1', 'Dataset1', 'Dataset1', 'Dataset1','Dataset2','Dataset2']
    id1 = ['exp1', 'exp2']
    id2 = ['session1', 'session2', 'session3', 'session4', 'session5', 'session6']
    for i in range(6):
        if i < 4:
            id = id1[0] + '_' + id2[i]
            hashkey1 = getSHA256(id1[0])
            hashkey2 = getSHA256(id2[i])
            hashkey = getSHA256(id)
            sql = "insert into staging.linkorganised values ('" + hashkey + "','" + source[i] + "','" + hashkey1 + "','" + hashkey2 + "');"
            cur.execute(sql)
            print("%s: %s <-> %s" % (id, id1[0], id2[i]))
        else:
            id = id1[1] + '_' + id2[i]
            hashkey1 = getSHA256(id1[1])
            hashkey2 = getSHA256(id2[i])
            hashkey = getSHA256(id)
            sql = "insert into staging.linkorganised values ('" + hashkey + "','" + source[i] + "','" + hashkey1 + "','" + hashkey2 + "');"
            cur.execute(sql)
            print("%s: %s <-> %s" % (id, id1[1], id2[i]))

    conn.commit()
    conn.close()
