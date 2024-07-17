# G. Ни больше ни меньше https://contest.yandex.ru/contest/59540/problems/G/

def splitter(n, arr):    
    cur_len, last_index, counter = 0, 0, 0
    res, minv = [], 1
    for i in range(n):
        minv = min(minv, arr[i])
        if minv >= cur_len + 1:
            if not cur_len: minv = arr[i]
            cur_len += 1
        else:
            res.append(cur_len)
            counter += 1
            minv = arr[i]
            cur_len = 1
            last_index = i
    res.append(n - last_index)
    return res

tests_count = 3
test_cases = (
    (5, (1, 3, 3, 3, 2)),
    (16, (1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9)),
    (7, (7, 2, 3, 4, 3, 2, 7))
)
tests_ans = ([1,3,1], [1,6,9], [2,3,2])
is_test = 1

if __name__ == '__main__':
    f =  splitter
    if is_test:
        for i in range(tests_count):
            try:
                assert f(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer\n your answer is  {f(*test_cases[i])}\n right answer is {tests_ans[i]}')
    else:
        for i in range(int(input())):
            n = int(input())
            arr = tuple(map(int, input().split()))
            res = splitter(n, arr)
            print(len(res))
            print(*res)