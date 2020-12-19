from pythonds.basic.stack import Stack

def binary(n):
	s = Stack()
	while n != 0:
		s.push(n % 2)
		n //= 2
	
	binstr = ''
	while not s.isEmpty():
		binstr += str(s.pop())
	
	return binstr
	

print(binary(int(input("decimal number:"))))
