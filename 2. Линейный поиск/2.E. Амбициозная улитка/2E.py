# E. Амбициозная улитка https://contest.yandex.ru/contest/59540/problems/E/

def max_height_solver(n, arr): 
    ups, downs = [], []
    for i in range(n):        
        (downs, ups)[arr[i][0] > arr[i][1]].append((arr[i][0], arr[i][1], i+1))        
    ups.sort(key=lambda x: x[1]), downs.sort(key=lambda x: -x[0]), ups.extend(downs)
    del downs
    m = ups[0][0]
    temp = m
    res = [ups[0][2]]
    for i in range(1, n):
        temp = temp - ups[i-1][1] + ups[i][0]
        m = max(temp, m)
        res.append(ups[i][2])
    return (m, res)

tests_count = 3
test_cases = (
    (3,((1,5), (8,2), (4,4))),
    (2,((7,6),(7,4))),
    (6,((822889311,446755913),(715477619,181424399),(61020590,573085537),(480845266,448565595),(135599877,389312924), (160714711,449656269)))
)
tests_ans = ((10, [2,3,1]), (10, [2,1]), (1391031884, [2, 1, 4, 6, 5, 3]))
is_test = 1

if __name__ == '__main__':
    f =  max_height_solver
    if is_test:
        for i in range(tests_count):
            try:
                assert f(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer\n your answer is  {f(*test_cases[i])}\n right answer is {tests_ans[i]}')
    else:
        n = int(input()) 
        arr = tuple(tuple(map(int, input().split())) for _ in range(n))
        res = f(n, arr)
        print(res[0])
        print(*res[1])