import json

def prob01(searchItems) :
    try :
        data = json.load(open("json0.json"))
        # print(len(data))
        for sItem in searchItems :
            data = data.get(sItem)
        return data
    except Exception:
        return ('error: ',Exception, type(Exception))
