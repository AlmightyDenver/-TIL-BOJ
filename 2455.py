station = []
total = 0
while True:
    mi, pl = map(int, input().split())
    if pl != 0:
        total += pl
        total -= mi
        station.append(total)
    else:
        total += pl
        total -= mi
        station.append(total)
        break
answer = max(station)
print(answer)
