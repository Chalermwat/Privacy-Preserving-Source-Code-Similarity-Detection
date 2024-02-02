import tokenize
import argparse
import ssdeep
import keyword

BUILT_IN_FUNC = ['abs','alter','all','anext','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','classmethod','compile','complex','delattr','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip']
TMP_FILENAME = "tmp"

def isBuiltIn(string):
    return string in BUILT_IN_FUNC

def preprocessing(filename):
    out=''
    o = open(TMP_FILENAME,'w')
    isMultiCommentStart=False
    isHeaderSection=True
    with open(filename, 'r') as f:
        for line in f:
            if isHeaderSection:
                if 'import' not in line: 
                    isHeaderSection=False
                    multicomment_start = line.find("'''")
                    multicomment_end = line.find("'''",multicomment_start+1)

                    if multicomment_start !=-1 and multicomment_end!=-1:
                        out+=line[:multicomment_start]+line[multicomment_end:]
                        continue

                    if multicomment_start !=-1: 
                        isMultiCommentStart=not isMultiCommentStart
                    else:
                        out+=line
            else:
                # Remove multiline comment
                multicomment_start = line.find("'''")
                multicomment_end = line.find("'''",multicomment_start+1)

                # Multiline comment end in one line
                if multicomment_start !=-1 and multicomment_end!=-1:
                    out+=line[:multicomment_start]+line[multicomment_end+3:]
                    continue

                # Found start of the multiline comment
                if multicomment_start !=-1: 
                    isMultiCommentStart = not isMultiCommentStart
                    if not isMultiCommentStart:
                        out+=line[multicomment_start+3:]
                else:
                    if not isMultiCommentStart:
                        out+=line
    o.write(out)

def processing(filename,static_var=False):
    code_section = ''
    var_map = {}
    func_map = {}
    var_index = 1
    func_index = 1
    isFuncName = False
    with open(filename, 'rb') as f:
        # Import section
        while True:
            last_read = f.tell()
            line=f.readline()
            if b'import' not in line: 
                f.seek(last_read)
                break

        # Code section
        tokens = list(tokenize.tokenize(f.readline))
        for index,token in enumerate(tokens):

            # Ignore comment newline encoding nl string indent
            if(token.type not in [4,6,61,62,63]): 
                # Token type is Name
                if(token.type==1):
                    # Token string is Keyword
                    if(keyword.iskeyword(token.string)):
                        if(token.string=='def'):
                            isFuncName=True
                        code_section+=token.string
                    # Token string is Built-in function name
                    elif(isBuiltIn(token.string)):
                        if(index+1<len(tokens)):
                            if(tokens[index+1].string=='('):
                                code_section+=token.string
                            else:
                                var_index = addToMap(token.string,var_index,var_map)
                                code_section+= var_map[token.string] if not static_var else 'V'
                        else:
                            var_index = addToMap(token.string,var_index,var_map)
                            code_section+= var_map[token.string] if not static_var else 'V'
                    # Token string is declare function name
                    elif(token.string in func_map):
                        if(index+1<len(tokens)):
                            if(tokens[index+1].string=='('):
                                code_section+= func_map[token.string] if not static_var else 'F'
                            else:
                                var_index = addToMap(token.string,var_index,var_map)
                                code_section+= var_map[token.string] if not static_var else 'V'
                        else:
                            var_index = addToMap(token.string,var_index,var_map)
                            code_section+= var_map[token.string] if not static_var else 'V'
                    # Token string is other name
                    else:
                        if(isFuncName):
                            func_index = addToMap(token.string,func_index,func_map,isVar=False)
                            code_section+= func_map[token.string] if not static_var else 'F'
                            isFuncName=False
                        else:
                            var_index = addToMap(token.string,var_index,var_map)
                            code_section+= var_map[token.string] if not static_var else 'V'
                else:
                    isFuncName=False
                    code_section+=token.string

    return code_section

def addToMap(key,index,map,isVar=True):
    if(key not in map):
        map[key]='V'+str(index) if isVar else 'F'+str(index)
        index+=1
    return index
    
def genFuzzyHash(string):
    return ssdeep.hash(string)

parser = argparse.ArgumentParser(description='Generate Fussy Hash')
parser.add_argument('filepath', metavar='FilePath', type=str,
                    help='File path to source code')

args = parser.parse_args()

if __name__ == "__main__":
    static_var=False
    prepro_code = preprocessing(args.filepath)
    process_code = processing(TMP_FILENAME,static_var)
    print(process_code)
    fuzzyHash = genFuzzyHash(process_code)
    print('Fuzzy hash:',fuzzyHash)



