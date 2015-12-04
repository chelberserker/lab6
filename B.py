with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        N = int(inp.readline())
        lis = list(map(int, inp.readline().split()))
        needfives = 0
        havefives = 0
        for i in range(N):
            if lis[i] == 5:
                havefives += 1
            else:
                havefives -= (lis[i]-5)//5
                if havefives < 0:
                    needfives -= havefives
                    havefives = 0
        print(needfives, file=out)
