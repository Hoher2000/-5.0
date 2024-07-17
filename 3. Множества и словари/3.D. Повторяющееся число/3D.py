# 3 D. Повторяющееся число https://contest.yandex.ru/contest/59541/problems/D/

def is_repeat(n, interval, arr):
    d = {}
    for i in range(n):
        d.setdefault(arr[i], None)
        if d[arr[i]] != None and i - d[arr[i]] <= interval:
            return 'YES'
        d[arr[i]] = i        
    return 'NO' 

tests_count = 3
test_cases = (
    (4, 2, (1, 2, 3, 1)),
    (4, 1, (1, 0, 1, 1)),
    (6, 2, (1, 2, 3, 1, 2, 3))
)
tests_ans = ('NO', 'YES', 'NO')
is_test = 1

if __name__ == '__main__':
    f =  is_repeat
    if is_test:
        for i in range(tests_count):
            try:
                assert f(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer\n your answer is  {f(*test_cases[i])}\n right answer is {tests_ans[i]}')
    else:
        n, interval = map(int, input().split())
        arr = tuple(map(int, input().split()))
        print(f(n, interval, arr))