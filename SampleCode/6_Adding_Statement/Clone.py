import json
filename = 'cipher'
#  Read the ciphertext file
with open(filename,'r') as c:
    payload = c.read()

#  Extract metadata (salt,alg)
payload = json.loads(payload)
data = payload['data']
salt = json.loads(data)['meta']['salt']
enc_alg = json.loads(data)['meta']['enc_alg'].lower()
key_alg = json.loads(data)['meta']['key_alg'].lower()
hmac_alg = json.loads(data)['meta']['hmac_alg'].lower()
iter = json.loads(data)['meta']['iter']