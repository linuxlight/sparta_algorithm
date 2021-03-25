shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()
    print(menus)

    for food in orders:
        is_in_menus = False
        current_min = 0
        current_max = len(menus)
        current_guess = (current_min + current_max) // 2
        while current_min <= current_max:
            if food is menus[current_guess]:
                is_in_menus = True
                break
            elif ord(food[0]) < ord(menus[current_guess][0]):
                current_max = current_guess - 1
            elif ord(food[0]) > ord(menus[current_guess][0]):
                current_min = current_guess + 1
            current_guess = (current_min + current_max) // 2
        if is_in_menus:
            continue
        else:
            return False
    return True



result = is_available_to_order(shop_menus, shop_orders)
print(result)