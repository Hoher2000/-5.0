# D. Слоны и ладьи https://contest.yandex.ru/contest/59539/problems/D/

from sys import stdin

def counter(desk_str):

    def r_go(x, y):
        nonlocal desk
        a = x+1
        while a < 8:
            if desk[a][y] not in 'RB':
                desk[a][y] = '#'
                a += 1
            else: break
        a = x-1
        while a > -1:
            if desk[a][y] not in 'RB':
                desk[a][y] = '#'
                a -= 1
            else: break
        a = y+1
        while a < 8:
            if desk[x][a] not in 'RB':
                desk[x][a] = '#'
                a += 1
            else: break
        a = y-1
        while a > -1:
            if desk[x][a] not in 'RB':
                desk[x][a] = '#'
                a -= 1
            else: break

    def b_go(x, y):
        nonlocal desk
        a, b = x+1, y+1
        while a < 8 and b < 8:
            if desk[a][b] not in 'RB':
                desk[a][b] = '#'
                a += 1
                b += 1
            else: break
        a, b = x+1, y-1
        while a < 8 and b > -1:
            if desk[a][b] not in 'RB':
                desk[a][b] = '#'
                a += 1
                b -= 1
            else: break
        a, b = x-1, y-1
        while a > -1 and b > -1:
            if desk[a][b] not in 'RB':
                desk[a][b] = '#'
                a -= 1
                b -= 1
            else: break
        a, b = x-1, y+1
        while a > -1 and b < 8:
            if desk[a][b] not in 'RB':
                desk[a][b] = '#'
                a -= 1
                b += 1
            else: break
    
    def count(desk):
        cnt = 0
        for i in desk: cnt += i.count('*')
        return cnt

    desk, R, B = [], [], []
    for i in range(8):
        desk.append(list(temp := desk_str[i][:8]))
        for j in range(8):
            if temp[j] == 'R': R.append((i, j))
            if temp[j] == 'B': B.append((i, j))

    if R:
        for i in R: r_go(*i)
    if B:
        for i in B: b_go(*i)
    return count(desk)

tests_count = 3
test_cases = (
    '''********
********
*R******
********
********
********
********
********''', 
    '''********
********
******B*
********
********
********
********
********''',
    '''********
*R******
********
*****B**
********
********
********
********'''
)
tests_ans = (49,54,40)
is_test = 1

if __name__ == '__main__':
    if is_test:
        for i in range(tests_count):
            assert counter(test_cases[i].splitlines()) == tests_ans[i]
    else:
        desk_str = stdin.readlines()
        print(counter(desk_str))