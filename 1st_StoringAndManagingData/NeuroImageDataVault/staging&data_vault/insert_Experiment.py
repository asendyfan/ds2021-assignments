import psycopg2
from code.staging.tools import getSHA256


def insert_Experiment(database='project', user='postgres', password='19980806', port='5432'):
    """insert experiment data"""
    print("\n*************Starting populating for Experiment*************\n")
    conn = psycopg2.connect(database=database, user=user, password=password, port=port)
    print("Connect database successfully!")
    cur = conn.cursor()

    source1 = 'Dataset1'
    id1 = 'exp1'
    hashkey1 = getSHA256(id1)
    title1 = "VisuoMotor Connectivity Experiment"
    goal1 = "Validating processing and analysis algorithms for fNIRS neuroimages"
    type1 = 'longitudinal'
    allocation1 = 'within-subject'

    source2 = 'Dataset2'
    id2 = 'exp2'
    hashkey2 = getSHA256(id2)
    title2 = "Multimodal Pre-autism Experiment"
    goal2 = "Studying biomedical markers of preautistic disorders"
    type2 = 'longitudinal'
    allocation2 = 'within-subject'

    sql = "insert into staging.experiment values('"+hashkey1+"','"+source1+"','"+id1+"','"+title1+"','"+goal1+"','"+type1+"','"+allocation1+"');"
    cur.execute(sql)
    sql = "insert into staging.experiment values('"+hashkey2+"','"+source2+"','"+id2+"','"+title2+"','"+goal2+"','"+type2+"','"+allocation2+"');"
    cur.execute(sql)

    conn.commit()
    conn.close()
