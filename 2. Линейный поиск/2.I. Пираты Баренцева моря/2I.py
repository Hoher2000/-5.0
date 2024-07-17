# I. Пираты Баренцева моря  https://contest.yandex.ru/contest/59540/problems/I/

from sys import stdin
from collections import deque

def ships_to_one_line(n, arr):    
    j_indexes = {}
    ships = sorted(arr)
    free_rows = list(range(1, n+1))
    for i, j in ships:
        j_indexes.setdefault(j, 0)
        j_indexes[j] += 1
        try: free_rows.remove(i)
        except: pass
    pivot_ind = round(sum(i*j for i, j in j_indexes.items()) / n)
    vars = []
    for p in range(pivot_ind-5, pivot_ind+5):
        free = deque(free_rows)
        pivot = [0] + [0 for i in range(n)]
        cnt = 0
        for i, j in ships:
            cnt += abs(j - p)
            pivot[i] += 1
        for i in range(1, n+1):
            while pivot[i] > 1:
                temp = free.popleft()
                pivot[i] -= 1
                cnt += abs(i-temp)
            if not free: break
        vars.append(cnt)
    return min(vars)

tests_count = 7
test_cases = [
    '''3
1 2
3 3
1 1''',
    '''10
9 4
8 9
5 4
10 8
7 9
10 5
9 2
8 10
3 9
6 2''',
    '''10
3 7
7 10
4 9
2 2
5 9
8 2
5 5
10 4
2 10
6 5''',
    '''10
4 4
10 2
5 5
5 1
1 8
9 3
9 6
8 5
1 9
4 5''',
    '''10
1 10
2 9
1 5
7 9
2 3
5 7
9 2
4 5
7 10
10 7''',
    '''10
8 7
1 1
3 3
2 1
6 9
1 8
10 4
2 8
9 2
4 6''',
    '''20
13 19
3 13
20 19
12 8
20 15
6 10
6 9
3 19
7 17
6 3
18 18
5 15
13 15
9 1
11 3
9 17
15 10
18 11
4 14
16 4'''
]
tests_ans = [3, 48, 32, 23, 30, 36, 108]
is_test = 1

if __name__ == '__main__':
    f =  ships_to_one_line
    if is_test:
        for i in range(tests_count):
            data = test_cases[i].splitlines()
            n = int(data[0])
            arr = tuple(tuple(map(int, j.split())) for j in data[1:n+1])
            try:
                assert f(n, arr) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer\n your answer is  {f(n, arr)}\n right answer is {tests_ans[i]}')
    else:
        data = stdin.readlines()
        n = int(data[0])
        arr = tuple(tuple(map(int, j.split())) for j in data[1:n+1])
        print(f(n, arr))