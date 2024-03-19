eq=input().split(' ')

class Stack():
	def __init__(self):
		self.S=[]
		self.top=-1
		
	def initialize(self):
		self.top=-1
	
	def isEmpty(self):
		if self.top==-1:
			return('Empty')
		else:
			return('Not Empty')
	
	def push(self,x):
		self.S.append(x)
		self.top+=1
	
	def pop(self):
		a=self.S[self.top]
		del self.S[self.top]
		self.top-=1
		return(a)
		
	
	
	
c=Stack()
for i in range(len(eq)):
	if eq[i].isdigit():
		c.push(eq[i])
	else:
		a=c.pop()
		b=c.pop()
		if eq[i]=='+':
			c.push(int(b)+int(a))
		elif eq[i]=='-':
			c.push(int(b)-int(a))
		else:
			c.push(int(b)*int(a))
			
print(c.pop())
