import matplotlib.pyplot as plt
import psycopg2
import numpy as np
import pandas as pd

database = 'project'
user = 'postgres'
password = ''

conn = psycopg2.connect(database=database, user=user, password='')


def CH(data, n):
    ch = np.empty((0, 1),float)
    for row in data:
        ch = np.append(ch, row[n-1]).astype(np.float64)
    ch = (ch-ch.mean())/(np.max(ch)-np.min(ch))
    return ch


def drawEEG(data, session, id):
    x = np.arange(len(data))
    fig, ax = plt.subplots(nrows=5, ncols=6, figsize=(25.6, 14.4))
    fig.suptitle('session'+str(session)+'-'+'eegid'+id)
    channel = 1
    for row in range(5):
        for col in range(6):
            print(channel)
            if row == 4 and col == 5:
                break
            tmp = ax[row][col]
            tmp.plot(x, CH(data, channel))
            tmp.set_xlabel('time')
            tmp.set_ylabel('value')
            tmp.set_title('CH' + str(channel))
            channel += 1

    plt.tight_layout()
    plt.savefig('session'+str(session)+'-'+'eegid'+id + '.png')
    print("Saved " + 'session'+str(session)+'-'+'eegid'+id + '.png')


for session in [1,2]:
    for i in range(1,44):
        id = str((session-1)*43+i)
        sql = "select eegdata from staging.eeg where eegdataid = 'eeg" + id + "';"
        eegdata = pd.read_sql(sql, con=conn)
        data = np.array(eegdata['eegdata'].values[0])
        data = data[:, 1:30]
        print(sql)
        print(data.shape)
        drawEEG(data, session, id)
'''id = '1'
sql = "select eegdata from staging.eeg where eegdataid = 'eeg" + id + "';"
eegdata = pd.read_sql(sql, con=conn)
data = np.array(eegdata['eegdata'].values[0])
print(data[0])'''

