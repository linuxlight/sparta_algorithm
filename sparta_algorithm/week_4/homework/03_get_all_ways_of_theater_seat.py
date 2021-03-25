seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programing(n, fibo_memo):
    # 각 seat slice 별 경우의 수는 피보나치 수열을 따릅니다.
    if n in fibo_memo:
        return fibo_memo[n]

    fibo_memo[n] = fibo_dynamic_programing(n-1, fibo_memo) + fibo_dynamic_programing(n-2, fibo_memo)
    return fibo_memo[n]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    seats_slices = []
    seats = []
    # vip석을 기준으로 자리를 나눕니다.
    for i in range(1, total_count+1):
        if i in fixed_seat_array:
            seats_slices.append(seats)
            seats = []
        else:
            seats.append(i)
    seats_slices.append(seats)

    # 각 slice 별 경우의 수
    cases_list = []
    for piece in seats_slices:
        case = fibo_dynamic_programing(len(piece), memo)
        cases_list.append(case)

    total_cases = 1
    for case in cases_list:
        total_cases *= case
    return total_cases


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))


'''
1
1개

원본:1
1 2
    21
2개

원본:12 
12 3
    1 32
원본:21
21 3
3개

원본:123
123 4
    12 43
원본:132
132 4
원본:213
213 4
    21 43
5개

원본:1234
1234 5
    123 54
원본:1243
1243 5
원본:1324
1324 5
    132 54
원본:2134
2134 5
    213 54
원본:2143
    2143 5
8개

원본:12345
12345 6
    1234 65
원본:12354
12354 6
원본:12435
12435 6
    12436 5
원본:13245
13245 6
    1324 65
원본:13254
13254 6
원본:21345
21345 6
    2134 65
원본:21354
21354 6
원본:21435
21435 6
    2143 65
13개
'''
