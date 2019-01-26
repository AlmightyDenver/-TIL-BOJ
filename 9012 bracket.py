n = int(input())
bracket = [input() for _ in range(n)]
for i in range(len(bracket)):
    if bracket[i][0] == ')' or bracket[i][-1] == '(':
        print('NO')
    else:
        cnt = 1
        for j in range(1, len(bracket[i])):
            while cnt >= 0 and j < len(bracket[i]):
                if bracket[i][j] == '(':
                    cnt += 1
                    j += 1
                elif bracket[i][j] == ')':
                    cnt -= 1
                    j += 1
            break
        print('NO') if cnt != 0 else print('YES')
