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
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a