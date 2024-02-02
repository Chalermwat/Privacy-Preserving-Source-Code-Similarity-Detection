# Privacy-Preserving-Source-Code-Similarity-Detection
The application can detect the similarity even if there is a change as follows:
1. Adding Whitespace
2. Adding Comment
3. Adding Multiline comment
4. Changing variable name
5. Changing Function name

## Client:
```
cd Client
python client.py ../SampleCode/1_WhiteSpace/Python1.py
```

```
usage: client.py [-h] FilePath

Generate Fussy Hash

positional arguments:
  FilePath    File path to source code

options:
  -h, --help  show this help message and exit
```

## Server:
```
cd Server
python server.py 
```

## How to get the similarity score
- Go to http://127.0.0.1:3000/
- Fill the hash from client.py
