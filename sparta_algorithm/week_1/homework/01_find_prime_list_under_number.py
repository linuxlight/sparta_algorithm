input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list=[]
    for num in range(2, number):
        for prime in range(2, num):
            if not num == prime and num % prime == 0:
                break
        else:
            prime_list += [num]
    return prime_list


result = find_prime_list_under_number(input)
print(result)