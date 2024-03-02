
#  Read the ciphertext file
with open(filename,'r') as c:
    payload = c.read()

#  Extract metadata (salt,alg)
payload = json.loads(payload)
iter = json.loads(payload['data'])['meta']['iter']
hmac_alg = json.loads(payload['data'])['meta']['hmac_alg'].lower()
key_alg = json.loads(payload['data'])['meta']['key_alg'].lower()
enc_alg = json.loads(payload['data'])['meta']['enc_alg'].lower()
salt = json.loads(payload['data'])['meta']['salt']





#  Generate key from password
_,enc_key,hmac_key = key.generateFromPass(password,enc_alg,iter,key_alg,salt)

#  Calculate HMAC from given password
cal_hmac = mac(hmac_key,payload['data'],hmac_alg)
