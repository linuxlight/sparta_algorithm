input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    sum = 0
    for element in array:
        if array.index(element) == 0:
            sum = element
        if sum + element < sum * element:
            sum *= element
        else:
            sum += element
    return sum


result = find_max_plus_or_multiply(input)
print(result)