# A. Минимальный прямоугольник https://contest.yandex.ru/contest/59540/problems/?nc=ZjTxAkCQ

from sys import stdin

def min_rect(arr):
		xl, yl = [], []
		for x, y in arr:
				xl.append(x)
				yl.append(y)
		return f'{min(xl)} {min(yl)} {max(xl)} {max(yl)}'

tests_count = 1
test_cases = (((1,3), (3,1), (3,5), (6,3)),)
tests_ans = ('1 1 6 5',)
is_test = True

if __name__ == '__main__':
    if is_test:
        for i in range(tests_count):
            try:
                assert min_rect(test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer: your answer is {f(test_cases[i])}, right answer is {tests_ans[i]}')
    else:
        d = tuple(tuple(int(j) for j in i.split()) for i in stdin.read().splitlines()[1:])
        print(min_rect(d))