import configparser
config = configparser.ConfigParser()


print(config.sections())
print(config.read('x.ini'))
print(config.sections())
print('bb' in config)
print('bytebong.com' in config)
print(config['DEFAULT']['User'])
print(config['DEFAULT']['Compression'])
topsecret = config['topsecret.server.com']

print(topsecret['ForwardX11'])
print(topsecret['Port'])

#for key in config['bitbucket.org']:
#	print(key)

#print(user)
#print(compressionlevel)
#print(serveraliveinterval)
#print(compression)
#print(forwardx11)

# print(config['bitbucket.org']['ForwardX11'])
