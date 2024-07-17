# 3 B. Анаграмма? https://contest.yandex.ru/contest/59541/problems/B/?success=113428209#30404/2022_09_07/LkNuPGKfMj

def is_anagramm(word1, word2):
		letters1, letters2 = dict(), dict()
		if (n := len(word1)) == len(word2):
				for i in range(n):
						letters1.setdefault(word1[i], 0)
						letters2.setdefault(word2[i], 0)
						letters1[word1[i]] += 1
						letters2[word2[i]] += 1
				return ('NO', 'YES')[letters1 == letters2]
		return 'NO'
		
tests_count = 2
test_cases = (
    ('dusty', 'study'),
    ('rat', 'bat')
)
tests_ans = ('YES', 'NO')
is_test = 1

if __name__ == '__main__':
    f =  is_anagramm
    if is_test:
        for i in range(tests_count):
            try:
                assert f(*test_cases[i]) == tests_ans[i]
            except:
                print(f'in test_ case #{i+1} is wrong answer\n your answer is  {f(*test_cases[i])}\n right answer is {tests_ans[i]}')
    else:
        print(is_anagramm(input(), input()))