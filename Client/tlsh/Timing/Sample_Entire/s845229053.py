"""
スタックのデータ構造の定義
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def individual_push(self, num):
        self.stack.append(num)

    def pop(self):
        if len(self.stack) > 0:
            return True, self.stack.pop(-1)
        else:
            return False, 0
    
    def push_individual(self, left_index, current_index):
        sum_a = 0
        for pair in reversed(self.stack):
            if pair[0] > left_index:
                _, a = self.pop()
                sum_a += a[1]
            else:
                break
        self.push((left_index, sum_a + (current_index - left_index)))

    def print_individual_volume(self):
        volume_list = [str(s[1]) for s in self.stack]
        if len(volume_list) == 0:
            print(0)
        else:
            print("{} ".format(len(volume_list)) + " ".join(volume_list))


if __name__=="__main__":
    input_values = input()

    stack1 = Stack()
    stack2 = Stack()
    area_sum = 0

    for i, v in enumerate(input_values):
        # print(i)

        if v == "\\":
            stack1.push(i)
        elif v == "/":
            result, pop_value = stack1.pop()
            if result:
                area = i - pop_value
                stack2.push_individual(pop_value, i)
            else:
                area = 0
            area_sum += area

    print(area_sum)
    stack2.print_individual_volume()
