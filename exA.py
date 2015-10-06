n = int(input())
A = input().split()
for i in range(n):
	A[i]=int(A[i])
A.append(' ')	
for i in range(n):
	for j in range(i, n):
		if A[i+1]==A[j]: 
				el=A[i]
print(el)

	
