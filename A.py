input = open('input.txt', 'r')
output = open('output.txt', 'w')
n = input.read()
A = input().split()
for i in range(n):
	A[i]=int(A[i])
A.append(' ')	
for i in range(n):
	for j in range(i+1, n):
		if A[i]==A[j]:
			output.write(A[i])
			break
output.close()
	
