import json

def prob01(searchItems) :
    try :
        data = json.load(open("data/json01.json"))
        # print(len(data))
        for sItem in searchItems :
            data = data.get(sItem)
        return data
    except Exception:
        return ('error: ',Exception, type(Exception))


def prob02(searchItems,searchOptions) :
    array = []
    try :
        allData = json.load(open("data/json02.json"))
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

def prob04(sPath, dpath) :
    chArr = ['\'', 'u\'']
    spDict = {
        None : 'null',
        True : 'true',
        False : 'false',
    }

    f = open(sPath,'r')
    st = f.read()
    f.close()
    # print(st)
    # print(len(st))
    (i, counter) = (0, 1)

    # replacing:  '"' => '\"' , '\uffff' => '' , '\Uffffffff' => '' , '\xff' => ''
    while(i<len(st)) :
        if(st[i:i+1] == '\"') :
            # print('get \\"')
            st = st[0:i-1]+'\\'+st[i:len(st)]
            i += 2
        elif(st[i:i+2] == '\\u') :
            # print('get \\u')
            st = st.replace(st[i:i+6], '')
            i -= 1
        elif(st[i:i+2] == '\\U') :
            # print('get \\U')
            st = st.replace(st[i:i+10], '')
            i -= 1
        elif(st[i:i+2] == '\\x') :
            # print('get \\x')
            st = st.replace(st[i:i+4], '')
            i -= 1
        i += 1
    
    # replaceing u', ', None, True, False
    i = 0
    while(i<len(st)) :
        if(st[i:i+len(chArr[counter])] == chArr[counter]) :
            st = st.replace(st[i:i+len(chArr[counter])], '\"')
            i = i+len(chArr[counter])
            counter = (counter+1)%2

        for key in spDict :
            if(st[i:i+len(spDict[key])] == str(key)) :
                st = st.replace(st[i:i+len(spDict[key])], spDict[key])
                i += len(spDict[key])
        i += 1
    # print(st)
    f1 = open(dpath,'w')
    f1.write(st)
    f1.close()

    return("valid json data lies on data/outputdata/json04.json")


        
    