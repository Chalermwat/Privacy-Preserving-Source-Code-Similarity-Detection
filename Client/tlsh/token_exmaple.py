import tokenize

filename = './Example/example.py'
with open(filename, 'rb') as f:
    tokens = list(tokenize.tokenize(f.readline))
    for index,token in enumerate(tokens):
        print(token)