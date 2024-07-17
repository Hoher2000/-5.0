# 4 D. Рапорт https://contest.yandex.ru/contest/59542/problems/D/
# решение с использованием мнимого троичного поиска (ищем минимум функции бинпоиском)

def main():

    from sys import stdin

    def part_rows_counter(l, arr, n, min_len, max_len, counter = 1, i = 1):
        if l >= max_len: return (counter, max_len - l)
        if l < min_len: return (max_len, min_len - l)
        cur_len = arr[0]
        while i < n:
            if cur_len + arr[i] + 1 > l:
                counter += 1
                cur_len = arr[i]
            else:
              cur_len += arr[i] + 1
            i += 1
        return (counter, arr[i-1] - l)

    def raport_rows_counter(
        l, n, arr1, n1, min_len1, max_len1,
        arr2, n2, min_len2, max_len2
        ):
        return (
            max(
                part_rows_counter(l, arr1, n1, min_len1, max_len1),
                part_rows_counter(n-l, arr2, n2, min_len2, max_len2)
                )
            )

    def check_function(l, eps, *params):
        return raport_rows_counter(l+eps, *params) >= raport_rows_counter(l, *params)

    def fbinsearch(start, end, eps, check, *params):
        while start < end:
            mid = start + (end - start) // 2
            if check(mid, eps, *params):
                end = mid
            else:
                start = mid+1
        return start

    data = stdin.readlines()
    width, num_words1, num_words2 = map(int, data[0].split())
    len_words1 = []
    sum_len_words1 = 0
    min_len1 = 0
    data_words1 = data[1].split()

    for i in range(num_words1):
        temp = int(data_words1[i])
        len_words1.append(temp)
        sum_len_words1 += temp
        min_len1 = max(min_len1, temp)

    max_len1 = sum_len_words1 + num_words1 - 1

    len_words2 = []
    sum_len_words2 = 0
    min_len2 = 0
    data_words2 = data[2].split()

    for i in range(num_words2):
        temp = int(data_words2[i])
        len_words2.append(temp)
        sum_len_words2 += temp
        min_len2 = max(min_len2, temp)

    max_len2 = sum_len_words2 + num_words2 - 1

    eps = 1
    start = min_len1
    end = width-min_len2
    r = fbinsearch(
        start, end, eps, check_function, width, len_words1, num_words1, min_len1,
        max_len1, len_words2, num_words2, min_len2, max_len2
        )
    print(
        max(
            part_rows_counter(r, len_words1, num_words1, min_len1, max_len1),
            part_rows_counter(width-r, len_words2, num_words2, min_len2, max_len2)
            )[0]
        )

if __name__ == '__main__':
    main()       