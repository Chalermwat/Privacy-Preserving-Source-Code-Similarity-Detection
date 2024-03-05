import tokenize
import tlsh
import keyword
import os
import matplotlib.pyplot as plt


# Constant variable
BUILT_IN_FUNC = ['abs','alter','all','anext','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','classmethod','compile','complex','delattr','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip','__import__']
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

def processing(filename,static_var=False):
    code_section = ''
    import_section = set()
    var_map = {}
    func_map = {}
    # funcInput_map = {}
    funcVar_map = {}
    var_index = 1
    func_index = 1
    # funcInput_index = 1
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

            # print(token)
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
                    # print(line)
                    # print(funcVar_map)
                    # print(var_map)
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
                                if(isInFunc):
                                    funcVar_index = addToMap(token.string,funcVar_index,funcVar_map,"VAR")
                                    line+=funcVar_map[token.string]
                                else:
                                    var_index = addToMap(token.string,var_index,var_map,"VAR")
                                    line+= var_map[token.string] if not static_var else 'V'
                        else:
                            if(isInFunc):
                                    funcVar_index = addToMap(token.string,funcVar_index,funcVar_map,"VAR")
                                    line+=funcVar_map[token.string]
                            else:
                                var_index = addToMap(token.string,var_index,var_map,"VAR")
                                line+= var_map[token.string] if not static_var else 'V'

                    # Token string is declare function name
                    elif(token.string in func_map):
                        if(index+1<len(tokens)):
                            if(tokens[index+1].string=='('):
                                line+= func_map[token.string] if not static_var else 'F'
                            else:
                                if(isInFunc):
                                    funcVar_index = addToMap(token.string,funcVar_index,funcVar_map,"VAR")
                                    line+=funcVar_map[token.string]
                                else:
                                    var_index = addToMap(token.string,var_index,var_map,"VAR")
                                    line+= var_map[token.string] if not static_var else 'V'
                        else:
                            if(isInFunc):
                                funcVar_index = addToMap(token.string,funcVar_index,funcVar_map,"VAR")
                                line+=funcVar_map[token.string]
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
                            # funcInput_index = addToMap(token.string,funcInput_index,funcInput_map,"FUNC_INPUT")
                            # line+= funcInput_map[token.string]
                            funcVar_index = addToMap(token.string,funcVar_index,funcVar_map,"VAR")
                            line+=funcVar_map[token.string]
                        # Current string is in Func (Var in function)
                        elif(isInFunc):
                            funcVar_index = addToMap(token.string,funcVar_index,funcVar_map,"VAR")
                            line+=funcVar_map[token.string]
                            # line+=funcInput_map[token.string] if token.string in funcInput_map else funcVar_map[token.string]
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
    
def genFuzzyHash(string):
    return tlsh.hash(string.encode())


path = './1_512B.1024B'
dir_list = os.listdir(path)
static_var=False
hash_list=[]
for i in dir_list:
    filepath = path+'/'+i

    # With Normalized
    # prepro_code = removeMultilineComment(filepath)
    process_code = processing(filepath,static_var)
    fuzzyHash = genFuzzyHash(process_code)
    hash_list.append((i,fuzzyHash))

# path = './2_1024B.2048B'
# dir_list = os.listdir(path)
# static_var=False
# for i in dir_list:
#     filepath = path+'/'+i

#     # With Normalized
#     prepro_code = removeMultilineComment(filepath)
#     process_code = processing(TMP_FILENAME,static_var)
#     fuzzyHash = genFuzzyHash(process_code)
#     hash_list.append((i,fuzzyHash))

print(hash_list)
score_list=[]
for i in range(len(hash_list)-1):
    for j in range(i+1,len(hash_list)):
        hash1 = hash_list[i][1]
        hash2 = hash_list[j][1]
        score = tlsh.diffxlen(hash1,hash2)
        score_list.append((hash_list[i],hash_list[j],score))

s=0
s_list=[]
for i in score_list:
    # if i[2] < 150 : print(i)
    print(i[2])
    s_list.append(i[2])
    s+=i[2]

print(s/len(score_list))
print(f'Size: {len(score_list)}')
print(max(s_list),min(s_list))
# s_list.sort()
# print(len(BUILT_IN_FUNC))






