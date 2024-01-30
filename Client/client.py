import tokenize
import argparse
import ssdeep
import keyword

parser = argparse.ArgumentParser(description='Generate Fussy Hash')
parser.add_argument('filepath', metavar='FilePath', type=str,
                    help='File path to source code')

args = parser.parse_args()

buildin_func=['abs','alter','all','anext','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','classmethod','compile','complex','delattr','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip']

def isBuiltIn(string):
    return string in buildin_func

def preprocessing(filename,static_var=False):
    token_out = ''
    var_map = {}
    var_index = 1
    with open(filename, 'rb') as f:
        tokens = list(tokenize.tokenize(f.readline))
        # print(list(tokens))
        for index,token in enumerate(tokens):

            # Ignore comment newline encoding nl string indent
            if(token.type not in [3,4,6,61,62,63]): 
                if(token.type==1):
                    if(keyword.iskeyword(token.string)):
                        token_out+=token.string
                    elif(isBuiltIn(token.string)):
                        if(index+1<len(tokens)):
                            if(tokens[index+1].string=='('):
                                token_out+=token.string
                            else:
                                var_index = addToMap(token.string,var_index,var_map)
                                token_out+= var_map[token.string] if not static_var else 'V'
                        else:
                            var_index = addToMap(token.string,var_index,var_map)
                            token_out+= var_map[token.string] if not static_var else 'V'
                    else:
                        var_index = addToMap(token.string,var_index,var_map)
                        token_out+= var_map[token.string] if not static_var else 'V'
                else:
                    token_out+=token.string

    return token_out

def addToMap(key,index,map):
    if(key not in map):
        map[key]='V'+str(index)
        index+=1
    return index
    
def genFuzzyHash(string):
    return ssdeep.hash(string)

if __name__ == "__main__":
    static_var=False
    prepro_code = preprocessing(args.filepath,static_var)
    # print(prepro_code)
    fuzzyHash = genFuzzyHash(prepro_code)
    print('Fuzzy hash:',fuzzyHash)



