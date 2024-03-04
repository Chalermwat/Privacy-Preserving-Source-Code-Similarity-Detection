import key
from enc import *
from mac import *
import json
import argparse

def encrypt_mode(filename,password,**kwargs):
    #  Read the plaintext file
    with open(filename,'r') as f:
        data = f.read()

    enc_alg = kwargs['enc_alg'].lower()
    iter = kwargs['iter']
    outfile = kwargs['out']
    key_alg = kwargs['key_alg']
    hmac_alg = kwargs['hmac_alg']

    #  Generate key from password
    salt,enc_key,hmac_key = key.generateFromPass(password,enc_alg,iter,key_alg)

    # Encrypt the file with generated enc_key
    iv,ct = encryptFile(data,enc_key,enc_alg)

    #  Prepare the data for payload
    data = {
        'meta': {
            'salt': salt,
            'enc_alg':enc_alg,
            'key_alg':key_alg,
            'hmac_alg':hmac_alg,
            'iter':iter
        },
        'iv': iv,
        'ciphertext': ct
    }
    data_json = json.dumps(data)
 
    # Build the payload & add HMAC of data
    payload = {
        'data':data_json,
        'hmac': mac(hmac_key,data_json,hmac_alg)
    }
    payload_json = json.dumps(payload)

    # Write the payload to file
    with open(outfile+'.enc','w') as c:
        c.write(payload_json)
    
    print(f'Encrypting Success!!!')


def decrypt_mode(filename,password,outfile='plain'):
    #  Read the ciphertext file

    #  Read the ciphertext file
    with open(filename,'r') as c:
        payload = c.read()

    #  Extract metadata (salt,alg)
    payload = json.loads(payload)
    data = payload['data']
    iter = json.loads(data)['meta']['iter']
    hmac_alg = json.loads(data)['meta']['hmac_alg'].lower()
    key_alg = json.loads(data)['meta']['key_alg'].lower()
    enc_alg = json.loads(data)['meta']['enc_alg'].lower()
    salt = json.loads(data)['meta']['salt']




    #  Generate key from password
    _,enc_key,hmac_key = key.generateFromPass(password,enc_alg,iter,key_alg,salt)

    #  Calculate HMAC from given password
    cal_hmac = mac(hmac_key,payload['data'],hmac_alg)
    #  Verify hmac
    if verify(cal_hmac,payload['hmac']):
        #  If HMAC is matched, decrypt the file
        plaintext = decryptFile(payload['data'],enc_key,enc_alg)
        #  Write plaintext to file
        with open(outfile+'.dec','w') as p:
            p.write(plaintext)
    
        print(f'Decrypting Success!!!')
    else:
        #  If HMAC is not matched, display error
        print(f'Error: File is tampered or the password is incorrect.')
    
    

def args_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('MODE', metavar='MODE {encrypt,decrypt}',choices=['encrypt','decrypt'],help='Operation Mode')
    parser.add_argument('--enc_alg', choices=['des3','aes128','aes256','aes512'], help='Encryption algorithm (Default: AES256)')
    parser.add_argument('--key_alg', choices=['sha256','sha512'], help='PBKDF2 hash algorithm (Default: SHA256)')
    parser.add_argument('--hmac_alg', choices=['sha256','sha512'], help='HMAC hash algorithm (Default: SHA256)')
    parser.add_argument('--iter', type=int, help='Number of iterations used to generate Master Key (Default: 105000)')
    parser.add_argument('--out', help='Path for output file')

    parser.add_argument('PASSWORD', help='Password')
    parser.add_argument('FILEPATH', help='Path to the file')

    args = parser.parse_args()
    return args

args = args_parse()

password = args.PASSWORD
filename = args.FILEPATH

# Set default value
enc_alg = 'aes256'
key_alg = 'sha256'
hmac_alg = 'sha256'
outfile = 'out'
iter = 105000

if args.enc_alg:
    enc_alg = args.enc_alg.lower()
if args.iter:
    iter = args.iter
if args.out:
    outfile = args.out
if args.key_alg:
    key_alg = args.key_alg
if args.hmac_alg:
    hmac_alg = args.hmac_alg

if args.MODE.lower() == 'encrypt':
    encrypt_mode(filename,password,enc_alg=enc_alg,iter=iter,key_alg=key_alg,hmac_alg=hmac_alg,out=outfile)

elif args.MODE.lower() == 'decrypt':

    decrypt_mode(filename,password,outfile=outfile)


