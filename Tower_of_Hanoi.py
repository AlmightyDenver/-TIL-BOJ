import sys

def hanoi(N, Beg, Aux, End):
    if N == 1:
        print(Beg, End)
    elif N > 1:
        hanoi(N-1, Beg, End, Aux)
        hanoi(1, Beg, Aux, End)
        hanoi(N-1, Aux, Beg, End)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(2**N-1)
    if N <= 20:
        hanoi(N, 1,2,3)
