# Privacy-Preserving-Source-Code-Similarity-Detection
The idea of this application is to normalize the source code and then use Fuzzy hash(ssdeep) to detect the similarity.

The application can detect the similarity even if there is a change as follows:
1. Adding Whitespace
2. Adding Newline
3. Adding Indent
4. Adding Comment
5. Adding Multiline comment
6. Changing Variable name
7. Changing Function name
8. Duplicating Import_section
9. Rearrage Import_section

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
