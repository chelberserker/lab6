with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        N = int(inp.readline())
        lis = inp.readline().split()
        lis.sort()
        for i in range(N-1):
            if lis[i] == lis[i+1]:
                print(lis[i], file=out)
                break
