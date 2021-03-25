finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 이진탐색을 하기 위해서는 항상 정렬된 데이터에서만 가능하다.
def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    # 구현해보세요!
    for num in numbers:
        if num == target:
            return True
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)