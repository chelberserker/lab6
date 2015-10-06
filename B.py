input = open('input.txt', 'r')
output = open('output.txt', 'w')

k = 0
n = input.read()
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])
for i in range(n):
	if A[i] == 5:
		k -= 1
	A[i] -= 5
	k += A[i] // 5

print(k)
	
	
