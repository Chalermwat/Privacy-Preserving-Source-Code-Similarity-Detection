import sys #line:1
input_methods =['clipboard','file','key']#line:3
using_method =0 #line:4
input_method =input_methods [using_method ]#line:5
tin =lambda :map (int ,input ().split ())#line:7
lin =lambda :list (tin ())#line:8
mod =1000000007 #line:9
def main ():#line:13
	OOO0OOO00OOO00000 =int (input ())#line:14
	O00O0OOOO0OOOO00O =lin ()#line:17
	O00O0OOOO0OOOO00O .sort (reverse =True )#line:18
	return sum (O00O0OOOO0OOOO00O )-(2 *sum (O00O0OOOO0OOOO00O [1 ::2 ]))#line:19
isTest =False #line:24
def pa (O0OO0OOO0O0O0O00O ):#line:26
	if isTest :#line:27
		print (O0OO0OOO0O0O0O00O )#line:28
def input_clipboard ():#line:30
	import clipboard #line:31
	OO0000O0OO00OO00O =clipboard .get ()#line:32
	OOOO000O0OO0O0OO0 =OO0000O0OO00OO00O .splitlines ()#line:33
	for OO00O0000O00O0000 in OOOO000O0OO0O0OO0 :#line:34
		yield OO00O0000O00O0000 #line:35
if __name__ =="__main__":#line:37
	if sys .platform =='ios':#line:38
		if input_method ==input_methods [0 ]:#line:39
			ic =input_clipboard ()#line:40
			input =lambda :ic .__next__ ()#line:41
		elif input_method ==input_methods [1 ]:#line:42
			sys .stdin =open ('inputFile.txt')#line:43
		else :#line:44
			pass #line:45
		isTest =True #line:46
	else :#line:47
		pass #line:48
	ret =main ()#line:51
	if ret is not None :#line:52
		print (ret )