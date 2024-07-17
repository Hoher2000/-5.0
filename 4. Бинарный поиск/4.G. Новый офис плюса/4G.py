# 4 G. Новый офис плюса https://contest.yandex.ru/contest/59542/problems/G/ PyPy

def main():

    from sys import stdin 

    def is_all_good(i, j, s, table):
        if table[i][j][0] < 3 * s or table[i][j][1] < s: return False
        for dj in range(j+1, j+s):
            if table[i][dj][0] < 3 * s: return False
        if table[i+s][j-s][0] < s or table[i+s][j-s][1] < 3 * s: return False
        for di in range(i + s + 1, i + 2 * s):
            if table[di][j-s][1] < s * 3: return False
        return True


    def ch_funct(s, n, m, table):
        for i in range(n - 3 * s + 1):
            for j in range(s, m - 2 * s + 1):
                if is_all_good(i, j, s, table):
                    return True
        return False


    def rbinsearch(start, end, check, *params):
        while start != end:
            mid = (end + start + 1) // 2
            if check(mid, *params):
                start = mid
            else:
                end = mid - 1
        return start

    data = stdin.readlines()

    n, m = map(int, data[0].split())
    area = data[1:1+n]
    good_place_counter = [[None for j in range(m)] for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                good_place_counter[i][j] = (1, 1) if area[i][j] == '#' else (0, 0)
            elif i == n-1 and j < m-1:
                good_place_counter[i][j] = (1, 1 + good_place_counter[i][j+1][1]) if area[i][j] == '#' else (0, 0)
            elif i < n-1 and j == m-1:
                good_place_counter[i][j] = (1 + good_place_counter[i+1][j][0], 1) if area[i][j] == '#' else (0, 0)
            else:
                good_place_counter[i][j] = (1 + good_place_counter[i+1][j][0], 1 + good_place_counter[i][j+1][1]) if area[i][j] == '#' else (0, 0)

    print(rbinsearch(1, min(n,m)//3, ch_funct, n, m, good_place_counter))

if __name__ == '__main__':
    main()      