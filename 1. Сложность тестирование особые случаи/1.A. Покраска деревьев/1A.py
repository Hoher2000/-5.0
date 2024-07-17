# https://contest.yandex.ru/contest/59539/problems/

def trees_counter(p, v, q, m):
    m, v = (p - v, p + v), (q - m, q + m)
    minv, maxv = min(m, v), max(m, v)
    if maxv[0] > minv[1]: return minv[1] - minv[0]  +maxv[1] - maxv[0] + 2
    if maxv[1] <= minv[1]: return minv[1] - minv[0] + 1
    return maxv[1] - minv[0] + 1

tests_count = 1
test_cases = ((0, 7, 12, 5), )
tests_ans = (25, )
is_test = 0

if __name__ == '__main__':
    if is_test:
        for i in range(tests_count):
            assert trees_counter(*test_cases[i]) == tests_ans[i]
    else:
        p, v = map(int, input().split())
        q, m = map(int, input().split())
        print(trees_counter(p, v, q, m))