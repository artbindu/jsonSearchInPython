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


def prob02(searchItems,searchOptions) :
    array = []
    try :
        allData = json.load(open("json1.json"))
        for data in allData :
            # print(data)
            for x in searchItems :
                data = data.get(x)
            for y in searchOptions :
                fData = data.get(y)
                if(fData) :
                    array.append(fData)
                    break
        return array
    except :
        print('this is exception')
        return('error: ',Exception, type(Exception))