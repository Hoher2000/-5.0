# 3 C. Удаление чисел https://contest.yandex.ru/contest/59541/problems/C/?success=113429892#30404/2022_04_16/aHGhXYXSPp

def min_del_counter(n, arr):
    digit_dict = {}
    for d in arr:
        digit_dict.setdefault(d, 0)
        digit_dict[d] += 1
    mod_dict = sorted(digit_dict)
    k = len(mod_dict)
    if k == 1: return 0
    maxv = 0
    for i in range(1, k):
        if mod_dict[i] - 1 == mod_dict[i-1]:
            if digit_dict[mod_dict[i]] + digit_dict[mod_dict[i-1]] > maxv:
                ind = [mod_dict[i], mod_dict[i-1]]
                maxv = digit_dict[mod_dict[i]] + digit_dict[mod_dict[i-1]]
        else:
            if digit_dict[mod_dict[i]] > maxv:
                ind = [mod_dict[i]]
                maxv = digit_dict[mod_dict[i]]

    return sum(digit_dict[i] for i in digit_dict if i not in ind)

tests_count = 2
test_cases = (
    (5, (1, 2, 3, 4, 5)),
    (10, (1, 1, 2, 3, 5, 5, 2, 2, 1, 5))
)
tests_ans = (3, 4)
is_test = 1

if __name__ == '__main__':
    f =  min_del_counter
    if is_test:
        for i in range(tests_count):
            try:
                assert f(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer\n your answer is  {f(*test_cases[i])}\n right answer is {tests_ans[i]}')
    else:
        n = int(input())
        arr = tuple(map(int, input().split()))
        print(min_del_counter(n, arr))