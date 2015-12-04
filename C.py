with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        N = int(inp.readline())
        lis = list(map(int, inp.readline().split()))
        lmin = -1
        for i in range(N):
            if lis[i] > 0:
                continue
            itap = i
            tap = lis[i]
            while itap + 1 < len(lis):
                itap += 1
                if lis[itap] == -tap:
                    if lmin == -1 or lmin > len(lis[i:itap]):
                        lmin = len(lis[i:itap])
        if lmin == -1:
            print(0, file=out)
        else:
            print(lmin, file=out)
