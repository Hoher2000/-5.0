# https://contest.yandex.ru/contest/59539/problems/C/

from functools import lru_cache

def min_clisks_counter(n, arr):
    helper = lru_cache(lambda n: n // 4 + ((2, 1)[n % 4 == 1], 0)[n % 4 == 0])
    return sum(helper(i) for i in arr)

tests_count = 1
test_cases = ((5, [1,4,12,9,0]), )
tests_ans = (8,)
is_test = 1

if __name__ == '__main__':
    if is_test:
        for i in range(tests_count):
            assert min_clisks_counter(*test_cases[i]) == tests_ans[i]
    else:
        n = int(input())
        arr = [int(input()) for i in range(n)]
        print(min_clisks_counter(n, arr))