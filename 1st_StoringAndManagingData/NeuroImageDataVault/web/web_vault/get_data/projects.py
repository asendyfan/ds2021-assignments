# import jsonddf

# config = json.loads('db_config.json')
# print(config)

from .DBConnection import conn, excuteSql

def getProjectsList():
    cols = ['experimentid', 'title', 'goal', 'typebynumberofsessions', 'typebyallocation']
    sql = 'select {} from HubExperiment INNER JOIN SatExperiment ON HubExperiment.ExperimentHashKey=SatExperiment.ExperimentHashKey;'\
        .format(str(cols).replace('\'', '')).replace('[', '').replace(']', '')
    raw = excuteSql(sql)

    data = []
    for rawitem in raw:
        item = {}
        for i, col in enumerate(cols):
            item[col] = rawitem[i]
        data.append(item)
    # print(data)
    return data

def getProjectData(id):
    projects = getProjectsList()
    projectItem = [item for item in projects if item['experimentid'] == id]
    if (projectItem is None) or len(projectItem) == 0:
        return None
    projectItem = projectItem[0]
    
    return {
        'experiment':projectItem,
        'results':[
            {'desc':'xxx plot', 'imgurl':'/static/{}/Lena.png'.format(id)},
            {'desc':'xxx plot', 'imgurl':'/static/{}/cat.jpg'.format(id)},
            {'desc':'xxx plot', 'imgurl':'/static/{}/Lena.png'.format(id)},
            {'desc':'xxx plot', 'imgurl':'/static/{}/cat.jpg'.format(id)}
        ]
    }
