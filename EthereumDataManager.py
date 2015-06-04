import pycurl
from StringIO import StringIO

buffer = StringIO('{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}')
c = pycurl.Curl()
c.setopt(c.URL, 'localhost:8545')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body)