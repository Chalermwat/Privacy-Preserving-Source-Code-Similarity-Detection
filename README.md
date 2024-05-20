# Privacy-Preserving-Source-Code-Similarity-Detection
The idea of this application is to normalize the source code and then use Fuzzy hash(TLSH) to detect the similarity.

The application can detect the similarity even if there is a change as follows:
1. Adding Whitespace
2. Adding Newline
3. Adding Indent
4. Adding Comment
5. Changing Variable name
6. Changing Function name
7. Duplicating Import_section
8. Rearrage Import_section

## Client:
```
cd Client/tlsh/
python client.py ../../SampleCode/1_\ Whitespace,\ newline,\ indent,\ comment/Original.py 
```

```
usage: client.py [-h] [--line LINE] FilePath

Generate Fussy Hash

positional arguments:
  FilePath     File path to source code

options:
  -h, --help   show this help message and exit
  --line LINE  Number of Line to split (default: 10)
```

## Server:
```
cd Server
python server_tlsh.py
```

## How to get the similarity score
- (For Entire File mode) Go to http://127.0.0.1:3000/
- (For Splitting Line mode) Go to http://127.0.0.1:3000/split
- Fill the hash from client.py

