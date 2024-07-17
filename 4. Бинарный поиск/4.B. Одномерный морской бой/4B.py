# 4 B. Одномерный морской бой https://contest.yandex.ru/contest/59542/problems/B/

def main():

    check_capacity = lambda k, n: 6 * n >= k * (k + 1) * (k + 2) + 3* k * (k + 1) - 6

    def rbinsearch(start, end, check, *params):
        while start != end:
            mid = (end + start + 1) // 2
            if check(mid, *params):
                start = mid
            else:
                end = mid - 1
        return start

    n = int(input())
    print(rbinsearch(0, n, check_capacity, n))

if __name__ == '__main__':
    main() 