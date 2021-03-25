import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


class Factory:
    today = 0

    def __init__(self):
        self.stock = ramen_stock
        self.__selected_tuples = []  # 선택된 보급물자 날짜 저장
        self.total_supplies = self.stock  # 현재 재고 supplies들의 총 합

    def do_minimum_case(self, heap):
        while self.total_supplies < supply_recover_k:
            # 최대 공급 가능 물자부터 받음
            temp_tup = heap.pop()
            # heap에 더 이상 보급가능 물자가 없다면?
            if temp_tup is None:
                print("보급가능 물자 소진, 파산")
                exit()
            supply, _ = temp_tup
            self.total_supplies += supply
            self.__selected_tuples.append(temp_tup)

    def make_product(self):
        self.stock -= 1

    def __is_out_of_stock(self):
        # 설마 재고가 다 떨어졌나요?
        if self.stock <= 0:
            return True
        else:
            return False

    def refill_stock(self, heap):
        for sel_sup, sel_date in self.__selected_tuples:
            if Factory.today == sel_date:
                self.stock += sel_sup
        if self.__is_out_of_stock():
            # 재고가 다 떨어졌네요. 예전에 받지 그랬어요?
            self.__back_to_supply_date(heap)

    def __back_to_supply_date(self, heap):
        temp_tup = heap.pop()
        # heap에 더 이상 보급가능 물자가 없다면?
        if temp_tup is None:
            print("보급가능 물자 소진, 파산")
            exit()
        supply, date = temp_tup
        if date <= Factory.today:
            self.__selected_tuples.append(temp_tup)
            # 오늘로부터 과거의 보급가능 날짜간의 거리
            difference = Factory.today - date
            # 예전으로 되돌아가요!
            Factory.today = date
            print("과거로!", str(Factory.today) + "째날")
            self.stock += difference
            self.stock += supply
            print("과거로 와서 리필받은 이후 stock", self.stock)
        else:
            # 되돌아 갈 수도 없네요.
            return "파산"

    def get_selected_tuples_length(self):
        return len(self.__selected_tuples)


class MaxTupleHeap:
    def __init__(self):
        self.heap = []

    def push_all(self, tuple_list):
        for tup in tuple_list:
            temp_tup = (-tup[0], tup[1])
            heapq.heappush(self.heap, temp_tup)

    def pop(self):
        if not self.is_empty():
            temp_tup = heapq.heappop(self.heap)
            return -temp_tup[0], temp_tup[1]
        else:
            print("Heap is empty!")
            return None

    def is_empty(self):
        if not self.heap:
            return True
        else:
            return False


def get_minimum_count_of_overseas_supply():
    # 풀어보세요!

    # supply랑 date를 tuple로 묶어버려요.
    my_tuple_list = get_tuple_list(supply_supplies, supply_dates)
    # 묶은 tuple을 max heap에 집어넣어요.
    my_heap = MaxTupleHeap()
    my_heap.push_all(my_tuple_list)

    # 공장을 가동해요.
    my_factory = Factory()
    # 우선 최소한의 보급 횟수를 구한다.
    my_factory.do_minimum_case(my_heap)

    while Factory.today < supply_recover_k:
        # 하루가 시작되었어요.
        Factory.today += 1
        # print("오늘은", str(Factory.today) + "째날")

        # 오늘 작업 시작전에 보급을 받을 시간이에요.
        my_factory.refill_stock(my_heap)

        # 오늘치를 생산했어요.
        my_factory.make_product()

        # 오늘의 결산이에요.
        # print("오늘의 생산 후 stock", my_factory.stock)

    return my_factory.get_selected_tuples_length()


def get_tuple_list(supplies, dates):
    tuple_list = []
    for i in range(len(dates)):
        tuple_list.append((supplies[i], dates[i]))
    return tuple_list


print(get_minimum_count_of_overseas_supply())
