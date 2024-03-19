def bubble_sort(a, n):
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1][1] > a[j][1]:
                a[j-1], a[j] = a[j], a[j-1]

    return a


def selection_sort(a, n):
    for i in range(n-1):
        min_j = i
        for j in range(i+1, n):
            if a[min_j][1] > a[j][1]:
                min_j = j
        if min_j != i:
            a[min_j], a[i] = a[i], a[min_j]

    return a


if __name__ == "__main__":
    n = int(input())
    a = input().split()

    result1 = bubble_sort(a[:], n)
    result2 = selection_sort(a[:], n)
    print(*result1)
    print("Stable")
    print(*result2)
    print("Stable" if result1 == result2 else "Not stable")
