import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(lambda x: (int(x[1]), x), input().split()))

    # Bubble Sort
    B = A.copy()
    at_least_once = True
    while at_least_once:
        at_least_once = False
        for i in range(N - 1):
            if B[i][0] > B[i + 1][0]:
                B[i], B[i + 1] = B[i + 1], B[i]
                at_least_once = True
    print(" ".join(map(lambda x: x[1], B)))
    print("Stable")

    # Selection Sort
    B = A.copy()
    stability = "Stable"
    for i in range(N - 1):
        min_j = i
        for j in range(i, N):
            if B[j][0] < B[min_j][0]:
                min_j = j
        if min_j != i:
            if B[i][0] in list(map(lambda x: x[0], B[i + 1: min_j])):
                stability = "Not stable"
            B[i], B[min_j] = B[min_j], B[i]
    print(" ".join(map(lambda x: x[1], B)))
    print(stability)


if __name__ == "__main__":
    main()

