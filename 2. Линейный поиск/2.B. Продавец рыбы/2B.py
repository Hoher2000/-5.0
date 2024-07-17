# B. Продавец рыбы https://contest.yandex.ru/contest/59540/problems/B/

def max_profit(n, k, arr):
    mp = 0
    for i in range(n-1):
        if (temp := max(arr[i+1:i+k+1]) - arr[i]) > mp: mp = temp
    return mp

tests_count = 2
test_cases = ((5,2,(1,2,3,4,5)), (5,2,(5,4,3,2,1)))
tests_ans = (2,0)
is_test = True

if __name__ == '__main__':
    if is_test:
        for i in range(tests_count):
            try:
                assert max_profit(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer: your answer is {f(*test_cases[i])}, right answer is {tests_ans[i]}')
    else:
        n, k = map(int, input().split())
        prices = tuple(map(int, input().split()))
        print(max_profit(n, k, prices))