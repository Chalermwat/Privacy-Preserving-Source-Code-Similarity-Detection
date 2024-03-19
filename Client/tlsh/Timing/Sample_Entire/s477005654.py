import sys

class Card:
    def __init__(self, kind, num):
        self.kind = kind
        self.num = num
    def __eq__(self, other):
        return (self.kind == other.kind) and (self.num == other.num)
    def __ne__(self, other):
        return not ((self.kind == other.kind) and (self.num == other.num))
    def __str__(self):
        return self.kind + self.num

def list_to_string(array):
    s = ""
    for n in array:
        s += str(n) + " "
    return s.strip()
    
def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def is_stable(array1, array2):
    if reduce(lambda x, y: x and y, map(lambda x: x[0] == x[1], zip(array1, array2))):
        return "Stable"
    else:
        return "Not stable"

def bubble_sort(array):
    for i in range(0, len(array)):
        for j in reversed(range(i+1, len(array))):
            if array[j].num < array[j-1].num:
                swap(array, j, j-1)
    return array
        
def selection_sort(array):
    for i in range(0, len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index].num > array[j].num:
                min_index = j
        swap(array, i, min_index)
    return array

def main():
    num = int(sys.stdin.readline().strip())
    array = map(lambda x: Card(x[0], x[1]), sys.stdin.readline().strip().split(" "))

    a = list(array)
    b = list(array)

    print list_to_string(bubble_sort(a))
    print "Stable"
    print list_to_string(selection_sort(b))
    print is_stable(a, b)

if __name__ == "__main__":
    main()