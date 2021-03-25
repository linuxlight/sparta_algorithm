current_r, current_c, current_d = 7, 4, 0  # r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class RobotVacuum:
    def __init__(self, r, c, d, room_map):
        self.r = r
        self.c = c
        self.d = d
        self.map = room_map
        self.is_isolated = False
        self.count = 0
        self.failed_to_move = False

    def procedure(self):
        self.__clean_current_spot()
        # 벽에 가로막혀 아예 움직일 수 없는 경우 중단.
        while not self.failed_to_move:
            self.__search_next_spot()
            if not self.is_isolated:
                # 움직일 수 있다면 움직인다.
                self.__move_to_next_spot()
                self.__clean_current_spot()
            else:
                # 움직일 수 없다면 돌아간다.
                # print("모든방향 청소완료, 후진한다.")
                self.__move_back()
            # print("current_d", self.d)
        self.print_current_room_map()

    def print_current_room_map(self):
        # 2는 현재 위치
        self.map[self.r][self.c] = 2
        for i in range(len(self.map)):
            print(self.map[i])
        # 9는 청소 완료된 구역
        self.map[self.r][self.c] = 9

    def __clean_current_spot(self):
        self.map[self.r][self.c] = 9
        self.count += 1

    def __search_next_spot(self):
        # 다음번 청소할 구역을 찾습니다.
        rotation_counter = 0
        # 방향에 따라 왼쪽 구역의 상태를 받아서 검사
        while self.__is_cleaned():
            # 청소 안 한 구역이 나올때까지 회전합니다.
            if self.d == 3:
                self.d = 0
            else:
                self.d += 1
            rotation_counter += 1
            # 한 바퀴 다 돌면 청소할 구역이 없는 것!
            if rotation_counter > 3:
                self.is_isolated = True
                return
        self.is_isolated = False

    def __move_to_next_spot(self):
        if self.d == 0:
            self.c -= 1
        elif self.d == 1:
            self.r += 1
        elif self.d == 2:
            self.c += 1
        elif self.d == 3:
            self.d = 0
            self.r -= 1
            return
        self.d += 1

    def __is_cleaned(self):
        target_spot = None
        # 방향에 따른 왼쪽 구역 상태 받아오기
        if self.d == 0:
            target_spot = self.map[self.r][self.c - 1]
        elif self.d == 1:
            target_spot = self.map[self.r + 1][self.c]
        elif self.d == 2:
            target_spot = self.map[self.r][self.c + 1]
        elif self.d == 3:
            target_spot = self.map[self.r - 1][self.c]
        # 왼쪽 구역의 상태를 검사
        if target_spot == 0:
            # 왼쪽 구역이 아직 청소가 되지 않았다.
            return False
        else:
            # 벽 또는 이미 청소된 구역이다.
            return True

    def __move_back(self):
        target_spot = None
        if self.d == 0:
            target_spot = self.map[self.r + 1][self.c]
            if target_spot != 1:
                self.r += 1
        elif self.d == 1:
            target_spot = self.map[self.r][self.c + 1]
            if target_spot != 1:
                self.c += 1
        elif self.d == 2:
            target_spot = self.map[self.r - 1][self.c]
            if target_spot != 1:
                self.r -= 1
        elif self.d == 3:
            target_spot = self.map[self.r][self.c - 1]
            if target_spot != 1:
                self.c -= 1
        if target_spot == 1:
            # print("벽에 막혀 뒤로 갈 수 없음.")
            self.failed_to_move = True


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    my_robot = RobotVacuum(r, c, d, room_map)
    my_robot.procedure()
    return my_robot.count


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))


'''
    로봇 청소기는 다음과 같이 작동한다.
    
    1. 현재 위치를 청소한다.
    2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
        a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.
    
    입력 조건
    로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. 이 때 d가 0인 경우에는 북쪽을, 
        1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
    
    또한 청소하고자 하는 방의 지도를 2차원 배열로 주어진다.
    빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.
    
    로봇 청소기가 있는 칸의 상태는 항상 빈 칸이라고 했을 때,
    로봇 청소기가 청소하는 칸의 개수를 반환하시오.
'''