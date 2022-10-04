#Задание 1

a = [1,0,3,4,0,6,7,8,9,0]
def summer(A):
	p = sum(A)
	print(p)
	
	
summer(a)

#задание 2

def unicorn(B):
	x= B.count(0)
	print(x)
	
	
unicorn(a)


#задание 3

def mermaid(n):
	for i in range(n):
		for j in range(i+1):
			print(j+1, end=' ')
		print()
			
mermaid(7)
			
#задание 4

def cleopatra(q):
	
	for i in range(1, q + 1):
		for j in range(1,q + 1-i):
			print(' ', end = ' ')
			
		for j in range (1,i + 1):
			print(j, end=' ')
			
		for j in range(i -1, 0, -1):
				print(j, end= ' ')
		print()
				
cleopatra(7)
				
				