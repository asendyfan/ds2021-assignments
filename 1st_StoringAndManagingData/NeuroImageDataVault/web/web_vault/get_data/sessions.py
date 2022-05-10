from .DBConnection import conn, excuteSql

def getSessions(experimentid):
    cols = ['experimentid', 'sessionid']
    sql = 'select {} from HubSession \
            INNER JOIN linkorganised ON linkorganised.sessionhashkey = HubSession.sessionhashkey\
            INNER JOIN hubexperiment ON hubexperiment.experimenthashkey = linkorganised.experimenthashkey\
            Where experimentid=\'{}\';'\
        .format(str(cols).replace('\'', '').replace('[', '').replace(']', ''), experimentid)
    # print(sql)
    raw = excuteSql(sql)
    data = []
    for rawitem in raw:
        item = {}
        for i, col in enumerate(cols):
            item[col] = rawitem[i]
        data.append(item)
    print(data)
    return data

    