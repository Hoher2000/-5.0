# 3 G. Построить квадрат https://contest.yandex.ru/contest/59541/problems/G/

def main():
    from math import dist

    def find_square(n, arr):
        points = []
        points_set = set()
        res = tuple()
        n_set = 0
        for point in arr:
            if point not in points_set:
                n_set += 1
                points.append(point)
                points_set.add(point)

        if n_set == 1:
            x, y = points[0]
            return ((x+1, y), (x+1, y+1), (x, y+1))

        for a in range(n_set-1):
            for c in range(a+1, n_set):
                A, C = points[a], points[c]
                xA, yA = A
                xC, yC = C
                dy = yA - yC
                dx = xC - xA
                d = (dx - dy) / 2
                B, D = ((round(xA+d), round(yC-d)), (round(xC-d), round(yA+d)))
                if dist(A, B) == dist(C, D):
                    v = set((B, D))
                    dots = v - points_set
                    if not dots: return tuple()
                    if len(dots) == 1: res = tuple(dots)
                    elif len(res) != 1: res = tuple(dots)
        return res

    n = int(input())
    arr = tuple(tuple(map(int, input().split())) for _ in range(n))
    res = find_square(n, arr)
    print(len(res))
    for i in res: print(*i)

if __name__ == '__main__':
    main()