# C. Петя, Маша и верёвочки https://contest.yandex.ru/contest/59540/problems/C/

def min_len(cuts):
    maxlen = max(cuts)
    sums = (s := sum(cuts)) - maxlen
    return (s, maxlen - sums)[sums < maxlen]

tests_count = 2
test_cases = ((1,5,2,1), (5,12,4,3))
tests_ans = (1,24)
is_test = 0

if __name__ == '__main__':
    if is_test:
        f = min_len
        for i in range(tests_count):
            try:
                assert f(test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer: your answer is {f(test_cases[i])}, right answer is {tests_ans[i]}')
    else:
        input()
        cuts = tuple(map(int, input().split()))
        print(min_len(cuts))