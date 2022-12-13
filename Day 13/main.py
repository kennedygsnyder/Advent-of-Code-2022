import ast

def check(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0 

    elif isinstance(a, int):
        a = [a]

    elif isinstance(b, int):
        b = [b]

    if (len(a) == len(b)):
        for i in range (len(a)):
            result = check(a[i], b[i]) 
            if result != 0:
                return result
        
        return 0

    elif len(a) < len(b):
        if (len(a) == 0):
            return 1

        for i in range (len(a)):
            result = check(a[i], b[i]) 
            if result != 0:
                return result
        
        return 1

    elif len(a) > len(b):
        if (len(b) == 0):
            return -1
        for i in range (len(b)):
            result = check(a[i], b[i]) 
            if result != 0:
                return result
        return -1

    return -1

sum = 0
curr_pair = 1
packets_array = []

with open('input.txt') as f:
    lines = f.readlines()

    for i in range(0, len(lines), 3):
        a = ast.literal_eval(lines[i])
        b = ast.literal_eval(lines[i + 1])
        packets_array.append(a)
        packets_array.append(b)

        if check(a,b) == 1:
            sum+=curr_pair
        
        curr_pair +=1

    print(sum)

    #PART 2
    def bubble_sort(array):
        n = len(array)

        for i in range(n):
            already_sorted = True

            for j in range(n - i - 1):
                if check(array[j], array[j + 1]) == -1:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    already_sorted = False

            if already_sorted:
                break

        return array

    packets_array.append([[2]])
    packets_array.append([[6]])

    divider_index_sum = 1
    sorted_array = bubble_sort(packets_array)
    for i in range(len(sorted_array)):
        if sorted_array[i] == [[2]] or sorted_array[i] == [[6]]:
            divider_index_sum *= i+1

    print(divider_index_sum)


