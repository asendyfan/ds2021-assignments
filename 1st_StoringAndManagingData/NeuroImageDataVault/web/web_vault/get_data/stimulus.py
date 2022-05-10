from .DBConnection import conn, excuteSql


def getStimulus(sessionid):
    sql='select stimulusid, stimuluslevel, sessionid from HubStimulus\
        INNER JOIN SatStimulus ON HubStimulus.StimulusHashkey=SatStimulus.StimulusHashkey\
        INNER JOIN linktreatment ON linktreatment.stimulushashkey = HubStimulus.StimulusHashkey\
        inner JOIN hubsession on hubsession.sessionhashkey = linktreatment.sessionhashkey\
        WHERE hubsession.sessionid = \'{}\';'.format(sessionid)
    cols = ['stimulusid', 'stimuluslevel', 'sessionid']
    raw = excuteSql(sql)
    data = []
    for rawitem in raw:
        item = {}
        for i, col in enumerate(cols):
            item[col] = rawitem[i]
        data.append(item)
    return data