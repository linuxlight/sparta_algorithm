numbers = [1, 1, 1, 1, 1]
target_number = 3
result = []
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(array):
        all_ways.append(current_sum)
        return

    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index], all_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index], all_ways)



def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    count = 0
    get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result)
    for num in result:
        if num is target:
            count +=1

    return count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!