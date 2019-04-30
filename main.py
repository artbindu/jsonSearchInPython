import config as config

# --------------problem 01--------------------------
'''
Search a Specific json data; like find out 'annLength from json0.json'
'''
data = config.prob01(['ann','annLength'])
print('annLength: ', data)

# ---------------problem 02-------------------------------
'''
find out all 'url'
so urls lies in, mongoDbConfig --> connection
                               --> url
'''
data = config.prob02(['mongoDbConfig'],['url','connection'])
print('urls: ', data)
