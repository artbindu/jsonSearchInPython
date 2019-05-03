import config as config


# --------------problem 01--------------------------
'''
Search a Specific json data; like find out 'annLength from json0.json'
'''
data = config.prob01(['ann','annLength'])
print('prob01: annLength: ', data)

# ---------------problem 02-------------------------------
'''
@Rajdipta Barman
find out all 'url'
so urls lies in, mongoDbConfig --> connection
                               --> url
'''
data = config.prob02(['mongoDbConfig'],['url','connection'])
print('prob02: urls: ', data)

# ---------------problem 03-------------------------------
'''
if you have a mongoDB collection data; then how to store it again into data base.
    Open 'Robo 3T' --> connect any machine --> create db & collection --> Insert Document (with in new Collection) --> copy a bunch of json data and paste
    if you direct copy a mongooDB data and paste then show err: 
                                                                Unable to parse JSON:
                                                                Expecting '{', at (1, 1)
                ---- because of '/* 1 */', '/* 78 */', '/* 789 */' etc
    So, this code is to remove this portion; i.e. filtering mongoo data and store into a valid json format
    procedure: 
        1.  First store the mongoodata in '.txt' format
        2.  This code read it character-by-character and remove ('/* n */'; for n=1,2,3,4...) portions
        3.  Store output into '.json' format : copy this file and paste with in 'Insert Document' collection
'''
# sourcepath && destinationPath
sms = config.prob03('data/json03.txt', 'data/outputData/json03.json')
print('prob03:  ', sms)

# -----------problem 04-------------------------------
'''
@Debarati Bera
    convert a json file in .txt format to .json valid format
'''
sms = config.prob04('data/json04.txt', 'data/outputData/json04.json')
print('prob04:  ', sms)
