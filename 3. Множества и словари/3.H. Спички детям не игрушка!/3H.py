# H. Спички детям не игрушка! https://contest.yandex.ru/contest/59541/problems/H/?success=114698672#30404/2024_03_12/V2s0zIARNK

def main():

    from sys import stdin

    def matches_to_replace(data):
        bef_set_slope, aft_set_slope = set(), set()
        bef_dict, aft_dict = {}, {}
        n = int(data[0])
        for i in range(n):
            x1, y1, x2, y2 = map(int, data[i+1].split())
            cords = (x1, y1, x2, y2) if (x1 ,y1) < (x2 ,y2) else (x2, y2, x1 ,y1)
            slope = (y2-y1)/(x2-x1) if x2 != x1 else 'inf'
            bef_set_slope.add(slope)
            bef_dict.setdefault(slope, [])
            bef_dict[slope].append(cords)
            x1, y1, x2, y2 = map(int, data[i+1+n].split())
            cords = (x1, y1, x2, y2) if (x1 ,y1) < (x2 ,y2) else (x2, y2, x1 ,y1)
            slope = (y2-y1)/(x2-x1) if x2 != x1 else 'inf'
            aft_set_slope.add(slope)
            aft_dict.setdefault(slope, [])
            aft_dict[slope].append(cords)

        if not (com_slope := bef_set_slope & aft_set_slope): return n

        bef_list = tuple(k for i, j in bef_dict.items() for k in j if i in com_slope)
        after_list = tuple(k for i, j in aft_dict.items() for k in j if i in com_slope)
        res = {}

        maxv = 1
        for i in bef_list:
            for j in after_list:
                x1, y1, x2, y2 = i
                x3, y3, x4, y4 = j
                d1, d2 = (x3 - x1, y3 - y1), (x4 - x2, y4 - y2)
                if d1 == d2:
                    res.setdefault(d1, 0)
                    res[d1] += 1
                    maxv = max(maxv, res[d1])

        return n - maxv

    data = stdin.readlines()
    print(matches_to_replace(data))

if __name__ == '__main__':
    main()    