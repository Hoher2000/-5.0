# 4 C. Саруман https://contest.yandex.ru/contest/59542/problems/C/

def main():

    from sys import stdin

    def lbinsearch(start, end, check, *params):
        while start != end:
            mid = (end + start) // 2
            if check(mid, *params):
                end = mid
            else:
                start = mid+1

        return start

    def check_orcs(i, arr, l, s, n):
        return arr[i+l] - arr[i] >= s if i+l < n else True

    data = stdin.readlines()

    n, m = map(int, data[0].split())
    sums = [0 for i in range(n+1)]
    shelves_data = data[1].split()
    shelves = []

    for i in range(n):
        temp = int(shelves_data[i])
        shelves.append(temp)
        sums[i+1] = sums[i] + temp

    requests = tuple(tuple(map(int, i.split())) for i in data[2:2+m])
    del data, shelves_data, temp

    res = []

    for r in requests:
        i = lbinsearch(0, n, check_orcs, sums, r[0], r[1], n+1)
        res.append(i+1 if i < n and sums[i+r[0]]-sums[i] == r[1] else -1)

    print(*res, sep='\n')

if __name__ == '__main__':
    main()     