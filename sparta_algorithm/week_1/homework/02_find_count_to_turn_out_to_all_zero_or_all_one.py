input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    flip_cnt_zero = 0
    flip_cnt_one = 0
    isflip = False

    # 0으로 flip
    for index in range(len(string)):
        if not isflip and not string[index] == '0':
            flip_cnt_zero += 1
            isflip = True
        if string[index] == '0':
            isflip = False
    isflip = False

    # 1로 flip
    for index in range(len(string)):
        if not isflip and not string[index] == '1':
            flip_cnt_one += 1
            isflip = True
        if string[index] == '1':
            isflip = False

    if flip_cnt_zero > flip_cnt_one:
        return flip_cnt_one
    else:
        return flip_cnt_zero


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
