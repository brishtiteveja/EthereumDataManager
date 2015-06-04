import pycurl, json
from pprint import pprint
from StringIO import StringIO

ethereum_url = 'localhost:8545'


def curl_req(url, data):
    storage = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.setopt(c.VERBOSE, False)
    c.perform()
    c.close()
    content = storage.getvalue()
    return content


# Getting Block Number
data_blockNumber = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}'

resp = curl_req(ethereum_url, data_blockNumber)
body = json.loads(resp)

blockNumber = int(body['result'], 16)
print blockNumber

# Getting Block by Number
blockNum = hex(45367)
data_blockByNumber = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":1}'
resp = curl_req(ethereum_url, data_blockByNumber)
body = json.loads(resp)
print body

