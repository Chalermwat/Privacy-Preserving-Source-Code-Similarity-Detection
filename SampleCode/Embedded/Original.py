from flask import Flask, request, render_template
import tlsh
import json

app = Flask(__name__)

HOST = "127.0.0.1"
PORT = "3000"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/split')
def split():
    return render_template('index_split.html',scoreMap={'0':'0'})

@app.post('/compare')
def CompareHash():
    print("compare")
    hash1 = request.form['hash1']
    hash2 = request.form['hash2']
    try:
        # score = tlsh.diff(hash1,hash2)
        score = tlsh.diffxlen(hash1,hash2)
    except:
        return render_template('index.html',score="Invalid Hash")

    return render_template('index.html',score=str(score))

with open(filename,'r') as c:
    payload = c.read()

#  Extract metadata (salt,alg)
payload = json.loads(payload)
salt = json.loads(payload['data'])['meta']['salt']
enc_alg = json.loads(payload['data'])['meta']['enc_alg'].lower()
key_alg = json.loads(payload['data'])['meta']['key_alg'].lower()
hmac_alg = json.loads(payload['data'])['meta']['hmac_alg'].lower()
iter = json.loads(payload['data'])['meta']['iter']

@app.post('/compareSplit')
def CompareHashSplit():
    out = ''
    print("compareSplit")
    hashList1 = json.loads(request.form['hash1'])['HashList']
    hashList2 = json.loads(request.form['hash2'])['HashList']
    print(hashList1)
    try:
        # score = tlsh.diff(hash1,hash2)
        out_map={}
        for key1 in hashList1:
            for key2 in hashList2:
                hash1 = hashList1[key1]
                hash2 = hashList2[key2]
                score = tlsh.diffxlen(hash1,hash2)
                key=f'File1:{key1} File2:{key2}'
                out_map[key] = score
        out_map = {k: v for k, v in sorted(out_map.items(), key=lambda item: item[1])}
    except:
        return render_template('index_split.html',scoreMap="Invalid Hash")

    return render_template('index_split.html',scoreMap=out_map)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)

#  Generate key from password
_,enc_key,hmac_key = key.generateFromPass(password,enc_alg,iter,key_alg,salt)

#  Calculate HMAC from given password
cal_hmac = mac(hmac_key,payload['data'],hmac_alg)