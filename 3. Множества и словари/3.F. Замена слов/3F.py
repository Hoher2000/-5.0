# 3 F. Замена слов https://contest.yandex.ru/contest/59541/problems/F/
# проходит только на PyPy

def replacer(words, text):
    d = {}
    for i in sorted(words, key=len):
        d.setdefault(i[0], [])
        for sub in d[i[0]]:
            if i.startswith(sub):
                break
        else:
            d[i[0]].append(i)

    for i in range(len(text)):
        if (temp := d.get(text[i][0], False)):
            for sub in temp:
                if text[i].startswith(sub):
                    text[i] = sub
                    break
    return ' '.join(text)

tests_count = 2
test_cases = (
    (('a', 'b'), 'abdafb basrt casds dsasa a'.split()),
    (('aa', 'bc', 'aaa'), 'a aa aaa bcd abcd'.split())
)
tests_ans = ('a b casds dsasa a', 'a aa aa bc abcd')
is_test = 1

if __name__ == '__main__':
    f =  replacer
    if is_test:
        for i in range(tests_count):
            try:
                assert f(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer\n your answer is  {f(*test_cases[i])}\n right answer is {tests_ans[i]}')
    else:
        words = input().split()
        text = input().split()
        print(f(words, text))    