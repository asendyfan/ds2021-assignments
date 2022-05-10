import matplotlib.pyplot as plt
import psycopg2
import numpy as np
import pandas as pd

database = 'project'
user = 'postgres'
password = ''

conn = psycopg2.connect(database=database, user=user, password='')


def drawHBA(data, session, endpoint, title):
    x = np.arange(len(data))
    fig, ax = plt.subplots(nrows=4, ncols=6, figsize=(25.6, 14.4))
    fig.suptitle(endpoint)
    channel = 1
    for row in range(4):
        for col in range(6):
            tmp = ax[row][col]
            tmp.plot(x, CH(data, channel))
            tmp.set_xlabel('time')
            tmp.set_ylabel('value')
            tmp.set_title('CH' + str(channel))
            channel += 1
    plt.tight_layout()
    plt.savefig(title+'_session'+str(session)+endpoint+'.png')
    print("Saved "+title+'_session'+str(session)+endpoint+'.png')


def drawMES(data, session, title):
    x = np.arange(len(data))
    fig1, ax1 = plt.subplots(nrows=4, ncols=6, figsize=(25.6, 14.4))
    fig1.suptitle('wave length 1')
    channel = 1
    for row in range(4):
        for col in range(6):
            tmp1 = ax1[row][col]
            tmp1.plot(x, CH(data, 2*channel-1))
            tmp1.set_xlabel('time')
            tmp1.set_ylabel('value')
            tmp1.set_title('CH' + str(channel))
            channel += 1
    plt.tight_layout()
    plt.savefig(title + '_session' + str(session) + 'mes' + '_wl1.png')
    print("Saved " + title + '_session' + str(session) + 'mes' + '_wl1.png')

    fig2, ax2 = plt.subplots(nrows=4, ncols=6, figsize=(25.6, 14.4))
    fig2.suptitle('wave length 2')
    channel = 1
    for row in range(4):
        for col in range(6):
            tmp2 = ax2[row][col]
            tmp2.plot(x, CH(data, 2 * channel))
            tmp2.set_xlabel('time')
            tmp2.set_ylabel('value')
            tmp2.set_title('CH' + str(channel))
            channel += 1
    plt.savefig(title + '_session' + str(session) + 'mes' + '_wl2.png')
    print("Saved " + title + '_session' + str(session) + 'mes' + '_wl2.png')


def CH(data, n):
    ch = np.empty((0, 1),float)
    for row in data:
        ch = np.append(ch, row[n-1]).astype(np.float64)
    return ch


def getMean_HBA(session, endpoint):
    mean = np.zeros((2801, 24), float)
    start = (session-1) * 10 + 1
    end = start + 10
    if session != 4:
        for i in range(start, end):
            sql = "select " + endpoint + " from staging.fnirs where fnirsdataid = 'fNIRS" + str(i) + '\';'
            print(sql)
            data = pd.read_sql(sql, con=conn)
            data = np.array(data[endpoint].values[0])
            data = data[1:,:24].astype(np.float64)
            mean += data/10
    else:
        for i in range(start, end-1):
            sql = "select " + endpoint + " from staging.fnirs where fnirsdataid = 'fNIRS" + str(i) + '\';'
            print(sql)
            data = pd.read_sql(sql, con=conn)
            data = np.array(data[endpoint].values[0])
            data = data[1:,:24].astype(np.float64)
            mean += data/9
    return mean


def getMean_Mes(session):
    mean = np.zeros((2851, 48), float)
    start = (session - 1) * 10 + 1
    end = start + 10
    for i in range(start, end):
        sql = "select mes from staging.fnirs where fnirsdataid = 'fNIRS" + str(i) + '\';'
        print(sql)
        data = pd.read_sql(sql, con=conn)
        data = np.array(data['mes'].values[0])
        data = data[1:, :48].astype(np.float64)
        mean += data / 10
    return mean


# get mean
'''for session in [1, 2, 3, 4]:
    data_deoxy = getMean_HBA(session, 'deoxy')
    data_oxy = getMean_HBA(session, 'oxy')
    data_total = getMean_HBA(session, 'total')
    data_mes = getMean_Mes(session)
    drawHBA(data_deoxy, session, 'deoxy', 'mean')
    drawHBA(data_oxy, session, 'oxy', 'mean')
    drawHBA(data_total, session, 'total', 'mean')
    drawMES(data_mes, session, 'mean')'''

# get endpoints of a certain sample
data = pd.read_sql("select deoxy from staging.fnirs where fnirsdataid = 'fNIRS1';", con=conn)
data = data['deoxy'].values[0][1:]
drawHBA(data, 1, 'deoxy', 'patient1')
data = pd.read_sql("select oxy from staging.fnirs where fnirsdataid = 'fNIRS1';", con=conn)
data = data['oxy'].values[0][1:]
drawHBA(data, 1, 'oxy', 'patient1')
data = pd.read_sql("select total from staging.fnirs where fnirsdataid = 'fNIRS1';", con=conn)
data = data['total'].values[0][1:]
drawHBA(data, 1, 'total', 'patient1')
data = pd.read_sql("select mes from staging.fnirs where fnirsdataid = 'fNIRS1';", con=conn)
data = data['mes'].values[0][1:]
drawMES(data, 1, 'patient1')



