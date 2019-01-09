def half(list):
    list.sort()
    min = list[0]
    list.append(min // 2)
    return (list)


while True:
    X = int(input())
    sticks = [64]
    count = 0

    if sum(sticks) == X:
        count = 1

    while sum(sticks) != X:
        if sum(sticks) > X:
            half(sticks)
            del sticks[0]
        else:
            half(sticks)
        count = len(sticks)
    print(count)
