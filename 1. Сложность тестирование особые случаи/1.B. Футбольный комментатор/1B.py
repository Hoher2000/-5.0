# https://contest.yandex.ru/contest/59539/problems/B/?success=111251123#30404/2020_11_05/i5qSOIJFWg

def goals_counter(p11, p21, p12, p22, home):
    delta = (p11 - p21 + p12 - p22)
    dh = p12 - p21 if home == 1 else p11 - p22
    if delta > 0: return 0
    if home == 1: return -delta + (delta >= dh)
    return -delta + (dh <= 0)

tests_count = 3
test_cases = ((0,0,0,0,1), (0,2,0,3,1), (0,2,0,3,2))
tests_ans = (1,5,6)
is_test = 1

if __name__ == '__main__':
    if is_test:
        for i in range(tests_count):
            assert goals_counter(*test_cases[i]) == tests_ans[i]
    else:
        p11, p21 = map(int, input().split(':'))
        p12, p22 = map(int, input().split(':'))
        home = int(input())
        print(goals_counter(p11, p21, p12, p22, home))