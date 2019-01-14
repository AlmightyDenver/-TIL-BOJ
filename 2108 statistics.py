n = int(input())
ARR = [int(input()) for i in range(n)]

ARR.sort()
avg = round(sum(ARR) / n)
median = ARR[n // 2]


def frequency(ARR):
    cnt = 0
    FREQ = []
    for i in range(n):
        new_cnt = ARR.count(ARR[i])
        if new_cnt > 1:
            if new_cnt > cnt:
                fre = i
                cnt = new_cnt
                FREQ.append(i)
            elif new_cnt == cnt and ARR[i] != ARR[i - 1]:
                FREQ.append(i)
            else:
                pass
    if len(FREQ) == 1:
        freq = ARR[FREQ[0]]
    elif len(FREQ) > 1:
        freq = ARR[FREQ[-2]]
    else:
        freq = ARR[1]
    return freq


def rge(ARR):
    if ARR[0] * ARR[-1] < 0:
        rge = abs(ARR[0]) + ARR[-1]
    else:
        rge = abs(ARR[-1] - ARR[0])
    return rge


print(avg)
print(median)
if n == 1:
    freq = ARR[0]
    rge = 0
else:
    freq = frequency(ARR)
    rge = rge(ARR)
print(freq)
print(rge)