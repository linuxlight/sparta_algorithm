genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    best_array = []
    my_genres = ListedGenres(genre_array)

    for index in range(len(genre_array)):
        my_genres.put(index, genre_array[index], play_array[index])

    my_genres.sort_by_played()
    for i in range(len(my_genres.reduced_genres)):
        for j, played in my_genres.get(i):
            best_array.append(j)
    return best_array


class LinkedSongs:
    def __init__(self, genre_name):
        self.genre_name = genre_name
        self.played_count = 0
        self.songs = []

    def add(self, index, value):
        self.songs.append((index, value))
        self.played_count += value

    def get(self):
        return self.songs

    def get_played_count(self):
        return self.played_count

    def sort_by_played(self):   # insertion sort, 내림차순
        for i in range(1, len(self.songs)):  # index : 1
            for j in range(i):
                (index1, played1) = self.songs[i - j - 1]
                (index2, played2) = self.songs[i - j]
                if played1 < played2:  # 총 played
                    self.songs[i - j - 1], self.songs[i - j] = self.songs[i - j], self.songs[i - j - 1]
                else:
                    break
        return


def avoid_duplicate(array):
    duplication_avoided = []
    copied_array = array[:]
    copied_array.sort()
    i = 0; j = 0
    while i < len(copied_array):
        if not duplication_avoided: # 초기조건
            duplication_avoided.append(copied_array[i])
        if copied_array[i] != duplication_avoided[j]:   # 배열 내 존재하지 않을 시 추가
            duplication_avoided.append(copied_array[i])
            j += 1
        i += 1
    return duplication_avoided


class ListedGenres:
    def __init__(self, array):
        self.items = []
        self.reduced_genres = avoid_duplicate(array)
        for g_name in self.reduced_genres:
            self.items.append(LinkedSongs(g_name))

    def put(self, index, key, value):
        for g_songs in self.items:
            if g_songs.genre_name == key:
                g_songs.add(index, value)
        return

    def get(self, key_index):
        return self.items[key_index].get()

    def get_played_count(self, key):
        for g_songs in self.items:
            if g_songs.genre_name == key:
                return g_songs.get_played_count()
        return None

    def sort_by_played(self):   # insertion sort, 내림차순
        for i in range(1, len(self.reduced_genres)):  # index : 1
            for j in range(i):
                if self.get_played_count(self.reduced_genres[i-j-1]) < self.get_played_count(self.reduced_genres[i-j]):  # 총 played
                    self.items[i-j-1], self.items[i-j] = self.items[i-j], self.items[i-j-1]
                else:
                    break
        for g_songs in self.items:
            g_songs.sort_by_played()
        return


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
