# Миша и математика https://contest.yandex.ru/contest/59539/problems/F/

def f(n, d):
    odd, odd_cnt = [], 0
    for i in range(n):
        if d[i] % 2:
            odd.append(i)
            odd_cnt += 1
    if odd_cnt % 2: return chr(43) * (n-1)
    for i in odd:
        if i + 1 < n and not d[i+1] % 2: return chr(43) * i + chr(120) + chr(43) * (n - 2 - i)
        if i - 1 >= 0 and not d[i-1] % 2: return chr(43) * (i-1) + chr(120) + chr(43) * (n - 1 - i)
    return chr(43) * (odd[0]-1) + chr(120) + chr(43) * (n - 2 - odd[0])

tests_count = 2
test_cases = ((3, (5,7,2)), (2, (4,-5)))
tests_ans = ('+x', '+')
is_test = True

if __name__ == '__main__':
    if is_test:
        for i in range(tests_count):
            try:
                assert f(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer: your answer is {f(*test_cases[i])}, right answer is {tests_ans[i]}')

    else:
        n = int(input())
        d = tuple(int(i) for i in input().split())
        print(f(n, d))