class Stack():
    def __init__(self):
        self.el = []
        
    def add(self, el):
        self.el.append(el)
        
    def pop(self):
        return self.el.pop()

    def isEmpty(self):
        if len(self.el) == 0:
            return True
        else:
            return False

        
a = raw_input().split()
#print a
st = Stack()

for index in range(len(a)):
    #print a[index]
    if a[index] in ['+', '-', '*']:
        num1 = st.pop()
        num2 = st.pop()
        if a[index] == '+':
            st.add(int(num1) + int(num2))
        elif a[index] == '-':
            st.add(int(num2) - int(num1))
        else:
            st.add(int(num1) * int(num2))
    else:
        st.add(a[index])
    #print st.el

ans = st.pop()
print ans