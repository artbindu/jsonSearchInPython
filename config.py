import json

def prob01(searchItems) :
    try :
        data = json.load(open("data/json0.json"))
        # print(len(data))
        for sItem in searchItems :
            data = data.get(sItem)
        return data
    except Exception:
        return ('error: ',Exception, type(Exception))


def prob02(searchItems,searchOptions) :
    array = []
    try :
        allData = json.load(open("data/json1.json"))
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

def prob03(sourcePath, destinationPath) :
    rfile = sourcePath
    f = open(rfile,'r')
    st = f.read()
    # print(st)
    # minLength = len(/* 2 */) = 7
    # maxLengrh = len(/* 1100 */) = 10
    (minLength, maxLength) = (7, 10)
    for i in range(minLength, maxLength+1) :
        j = 0
        count = pow(10,(i-7))
        while(j<len(st)) :
            if(count == pow(10,(i-6))) :
                print('done ',pow(10,(i-6)), ' json objects')
                break
            # remove '/* n */' parts for n=1,2,3,...
            sst = '/* '+str(count)+' */'
            if((st[j:j+i]) == sst) :
                st = st.replace(st[j:j+i], '')
                count += 1
            j += 1
    f.close()

    f1 = open(destinationPath,'w')
    f1.write(st)
    f1.close()
    return("paste 'json03.json' data with in 'new Mongoo Cloection'")
    