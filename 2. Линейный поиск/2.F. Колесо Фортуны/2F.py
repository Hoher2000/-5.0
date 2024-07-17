# 5F. Колесо Фортуны https://contest.yandex.ru/contest/59540/problems/F/

def max_win(n, arr, a, b, k):

    def check(n, index, a, b, k):
        for i in range(a, b + 1, k):
            if 0 < i % (n * k) - k * index <= k or 0 < i % (n * k) - k * (n - index) <= k:
                return True
        return False

    sectors = sorted([(i, j) for j, i in enumerate(arr)], key=lambda x: -x[0])
    for i, j in sectors:
        if check(n, j, a, b, k):
            return i

tests_count = 3
test_cases = (
    (5,(1,2,3,4,5),3,5,2),
    (5,(1,2,3,4,5),15,15,2),
    (5,(5,4,3,2,1),2,5,2)
)
tests_ans = (5,4,5)
is_test = 1

if __name__ == '__main__':
    f =  max_win
    if is_test:
        for i in range(tests_count):
            try:
                assert f(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer\n your answer is  {f(*test_cases[i])}\n right answer is {tests_ans[i]}')
    else:
        n = int(input()) 
        arr = tuple(map(int, input().split()))
        a, b, k = map(int, input().split())
        print(f(n, arr, a, b, k))