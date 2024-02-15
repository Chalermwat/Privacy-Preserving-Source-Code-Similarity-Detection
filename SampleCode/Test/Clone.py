import tokenize
import argparse
import tlsh
import keyword

# Constant variable
BUILT_IN_FUNC = ['abs','alter','all','anext','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','classmethod','compile','complex','delattr','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip']
TMP_FILENAME = "tmp"

def isBuiltIn(string):
    return string in BUILT_IN_FUNC

def removeMultilineComment(filename):
    out=''
    o = open(TMP_FILENAME,'w')
    isMultiCommentStart=False
    with open(filename, 'r') as f:
        for line in f:

            # Remove multiline comment
            multicomment_start = line.find("'''")
            multicomment_end = line.find("'''",multicomment_start+1)

            # Multiline comment end in one line
            if multicomment_start !=-1 and multicomment_end!=-1:
                out+=line[:multicomment_start]+line[multicomment_end+3:]
                continue

            # Found start of the multiline comment
            if multicomment_start !=-1 and line.find('"')!=multicomment_start-1: 
                isMultiCommentStart = not isMultiCommentStart
                if not isMultiCommentStart:
                    out+=line[multicomment_start+3:]
            else:
                if not isMultiCommentStart:
                    out+=line
    o.write(out)

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

def processing(filename,static_var=False):
    code_section = ''
    import_section = set()
    var_map = {}
    func_map = {}
    funcInput_map = {}
    funcVar_map = {}
    var_index = 1
    func_index = 1
    funcInput_index = 1
    funcVar_index = 1
    isFuncName = False
    indentAmount=0
    current_func_dedent=0
    isImportSection = False
    isFuncInput = False
    line=''
    isInFunc = False

    with open(filename, 'rb') as f:
        tokens = list(tokenize.tokenize(f.readline))
        for index,token in enumerate(tokens):
            # print(token)
            # Ignore comment nl encoding 
            # 61 = Comment
            # 62 = NL (New empty line)
            # 63 = Encoding (Start of file) 
            if(token.type not in [61,62,63]): 
                
                # Token type is New line
                if(token.type==4):
                    # Token is in Import section
                    if(isImportSection):
                        isImportSection=False
                        import_section.add(line.strip())
                    else:
                        # print('Line:',line)
                        code_section+=line.strip()+'\n'
                    line=''

                # Token type is Indent
                elif(token.type==5):
                    indentAmount+=1
                    line+='_'*indentAmount
                    
                # Token type is Dedent
                elif(token.type==6):
                    indentAmount-=1
                    # End of Function
                    if(isInFunc and current_func_dedent==indentAmount):
                        isInFunc=False
                        funcInput_map = {}
                        funcInput_index = 1
                        funcVar_map = {}
                        funcVar_index = 1

                # Token type is Name
                elif(token.type==1):

                    # Token string is Keyword
                    if(keyword.iskeyword(token.string)):
                        # Start of Function
                        if(token.string.lower()=='def'):
                            isFuncName=True
                            isInFunc=True
                            current_func_dedent = indentAmount
                        elif(token.string.lower()=='import' or token.string.lower()=='from'):
                            isImportSection=True
                        line+=token.string

                    # Token string is Built-in function name
                    elif(isBuiltIn(token.string)):
                        if(index+1<len(tokens)):
                            if(tokens[index+1].string=='('):
                                line+=token.string
                            else:
                                var_index = addToMap(token.string,var_index,var_map,"VAR")
                                line+= var_map[token.string] if not static_var else 'V'
                        else:
                            var_index = addToMap(token.string,var_index,var_map,"VAR")
                            line+= var_map[token.string] if not static_var else 'V'

                    # Token string is declare function name
                    elif(token.string in func_map):
                        if(index+1<len(tokens)):
                            if(tokens[index+1].string=='('):
                                line+= func_map[token.string] if not static_var else 'F'
                            else:
                                var_index = addToMap(token.string,var_index,var_map,"VAR")
                                line+= var_map[token.string] if not static_var else 'V'
                        else:
                            var_index = addToMap(token.string,var_index,var_map,"VAR")
                            line+= var_map[token.string] if not static_var else 'V'

                    # Token string is other name
                    else:
                        # Current string token is Func name
                        if(isFuncName):
                            func_index = addToMap(token.string,func_index,func_map,"FUNC")
                            line+= func_map[token.string] if not static_var else 'F'
                            isFuncName=False
                        # Current string token is in Import section
                        elif(isImportSection):
                            line+=token.string
                        # Current string token is Func input
                        elif (isFuncInput):
                            funcInput_index = addToMap(token.string,funcInput_index,funcInput_map,"FUNC_INPUT")
                            line+= funcInput_map[token.string]
                        # Current string is in Func (Var in function)
                        elif(isInFunc):
                            funcVar_index = addToMap(token.string,funcVar_index,funcVar_map,"VAR")
                            line+=funcInput_map[token.string] if token.string in funcInput_map else funcVar_map[token.string]
                        else:
                            var_index = addToMap(token.string,var_index,var_map,"VAR")
                            line+=var_map[token.string] if not static_var else 'V'
                # Token type is OP
                elif(token.type==54):
                    if(isInFunc):
                        if(token.string=='('):
                            isFuncInput=True
                        elif(token.string==')'):
                            isFuncInput=False
                    line+=token.string
                # Token is other type
                else:
                    line+=token.string
    
    # Sort Header
    import_section = list(import_section)
    import_section.sort()

    result = '\n'.join(import_section)+'\n' + code_section
    return result

def addToMap(key,index,map,type='VAR'):
    if(key not in map):
        if(type=='VAR'):
            map[key]='V'+str(index) 
        elif(type=='FUNC'):
            map[key]='F'+str(index) 
        elif(type=="FUNC_INPUT"):
            map[key]='I'+str(index) 
        index+=1
    return index
    
parser = argparse.ArgumentParser(description='Generate Fussy Hash')
parser.add_argument('filepath', metavar='FilePath', type=str,
                    help='File path to source code')

args = parser.parse_args()

def genFuzzyHash(filename):
    with open(filename, 'r') as f:
        code_string = ''.join(f.readlines())
    print(code_string)
    return tlsh.hash(code_string.encode())

if __name__ == "__main__":
    static_var=False
    prepro_code = removeMultilineComment(args.filepath)
    process_code = processing(TMP_FILENAME,static_var)
    print('\n******************** Normalized Code ********************')
    # print(process_code)
    print('*********************************************************\n')
    fuzzyHash = genFuzzyHash(process_code)
    print('Fuzzy hash:',fuzzyHash)