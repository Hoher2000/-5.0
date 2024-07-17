# 4 A. Быстрый поиск в массиве https://contest.yandex.ru/contest/59542/problems/

def main():
    from sys import stdin
    import bisect

    def how_much(array, start, end):
        return (bisect.bisect_right(array, end) - bisect.bisect_left(array, start))

    data = stdin.readlines()
    n, k = int(data[0]), int(data[2])
    array = sorted(map(int, data[1].split()))
    intervals = tuple(tuple(map(int, i.split())) for i in data[3:3+k])
    print(*(how_much(array, start, end) for start, end in intervals))

if __name__ == '__main__':
    main()   