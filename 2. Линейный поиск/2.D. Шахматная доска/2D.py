# D. Шахматная доска https://contest.yandex.ru/contest/59540/problems/D/

def perimetr(arr):

    def counter(i, j, desk):
        p = 4
        d = (-1, 0, 1, 0)
        for x in range(4):
            if desk[i+d[x]][j+d[3-x]] == 'x': p -= 1
        return p

    desk = [['*' for i in range(10)]for j in range(10)]
    for i, j in arr: desk[i][j] = 'x'
    return sum(counter(i, j, desk) for i, j in arr)

tests_count = 2
test_cases = (((1,1), (1,2), (2,1)), ((8,8),))
tests_ans = (8,4)
is_test = 0

if __name__ == '__main__':
    if is_test:
        f = perimetr
        for i in range(tests_count):
            try:
                assert f(test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer: your answer is {f(test_cases[i])}, right answer is {tests_ans[i]}')
    else:
        n = int(input()) 
        arr = tuple(tuple(map(int, input().split())) for _ in range(n))
        print(perimetr(arr))