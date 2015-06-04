import pycurl,json 
from StringIO import StringIO

data = json.dumps('{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}')

ethereum_url = 'localhost:8545'

c = pycurl.Curl()
c.setopt(c.URL, ethereum_url)
c.setopt(pycurl.HTTPHEADER, ['X-Postmark-Server-Token: API_TOKEN_HERE','Accept: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
response = c.perform()
print response
c.close()