import json
filename = 'cipher'
#  Read the ciphertext file
with open(filename,'r') as c:
    payload = c.read()

#  Extract metadata (salt,alg)
payload = json.loads(payload)

salt = json.loads(payload['data'])['meta']['salt']
enc_alg = json.loads(payload['data'])['meta']['enc_alg'].lower()
key_alg = json.loads(payload['data'])['meta']['key_alg'].lower()
hmac_alg = json.loads(payload['data'])['meta']['hmac_alg'].lower()
iter = json.loads(payload['data'])['meta']['iter']


