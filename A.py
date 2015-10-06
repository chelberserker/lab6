n = int(input())
A = input().split()
for i in range(n):
	A[i]=int(A[i])
A.append(' ')	
for i in range(n):
	for j in range(i+1, n):
		if A[i]==A[j]:
			print(A[i])
			break

	
