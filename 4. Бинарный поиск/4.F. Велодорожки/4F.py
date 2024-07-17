# 4 F. Велодорожки https://contest.yandex.ru/contest/59542/problems/F/ PyPy

def main():

    from sys import stdin
    import bisect

    def check_funct(s):
        nonlocal bad_y_by_lr_of_x, bad_x_arr, bad_x_count, height, width, bad_tales
        for i in range(bad_x_count):
            l = i
            r = bisect.bisect(bad_x_arr, bad_x_arr[i]+s-1)
            min_y = min(bad_y_by_lr_of_x[l][0], bad_y_by_lr_of_x[r-1][2])
            max_y = max(bad_y_by_lr_of_x[l][1], bad_y_by_lr_of_x[r-1][3])
            if max_y - min_y + 1 <= s: return True
        return False

    def lbinsearch(start, end, check, *params):
        while start != end:
            mid = (end + start) // 2
            if check(mid, *params):
                end = mid
            else:
                start = mid + 1
        return start

    data = stdin.readlines()
    width, height, n = map(int, data[0].split())
    bad_tales = sorted(tuple(int(j) for j in i.split()) for i in data[1:n+1])
    bad_x_count = len(set([i[0] for i in bad_tales]))
    bad_x_set = set()
    bad_y_by_lr_of_x = [[height+1, 0, height+1, 0] for i in range(bad_x_count)]
    bad_y_by_x = [[height+1, 0] for i in range(bad_x_count)]
    bad_x_arr = [0 for i in range(bad_x_count)]

    i = -1
    for tale in bad_tales:
        if tale[0] not in bad_x_set:
            bad_x_set.add(tale[0])
            i += 1
            bad_x_arr[i] = tale[0]
        old_y_min, old_y_max = bad_y_by_x[i][0], bad_y_by_x[i][1]
        bad_y_by_x[i][0], bad_y_by_x[i][1] = min(old_y_min, tale[1]), max(old_y_max, tale[1])


    for i in range(1, bad_x_count):
        bad_y_by_lr_of_x[i][0] = min(bad_y_by_lr_of_x[i-1][0], bad_y_by_x[i-1][0])
        bad_y_by_lr_of_x[i][1] = max(bad_y_by_lr_of_x[i-1][1], bad_y_by_x[i-1][1])
        bad_y_by_lr_of_x[bad_x_count-i-1][2] = min(bad_y_by_lr_of_x[bad_x_count-i][2], bad_y_by_x[bad_x_count-i][0])
        bad_y_by_lr_of_x[bad_x_count-i-1][3] = max(bad_y_by_lr_of_x[bad_x_count-i][3], bad_y_by_x[bad_x_count-i][1])


    print(lbinsearch(1, min(width, height), check_funct))

if __name__ == '__main__':
    main()     