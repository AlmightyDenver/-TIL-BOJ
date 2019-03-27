import sys

N, r, c = map(int, input().split(" "))

r += 1
c += 1
i = 1


def sabun(N, r, c, i, total):
    if N - i <= 0:
        if r == 2 and c == 2:
            total += 3
        elif r == 2 and c == 1:
            total += 2
        elif r == 1 and c == 2:
            total += 1
        return total

    else:
        half = 2 ** (N - i)
        kan = ((2 ** (N - i)) ** 2)
        if c - half > 0:
            total += kan
            c -= half
        if r - half > 0:
            total += 2 * kan
            r -= half
        i += 1
        return sabun(N, r, c, i, total)


if __name__ == "__main__":
    total = 0
    print(sabun(N, r, c, i, total))

