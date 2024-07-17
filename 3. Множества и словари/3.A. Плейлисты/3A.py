# 3 A. Плейлисты  https://contest.yandex.ru/contest/59541/problems/?success=113425882#30404/2022_04_16/5VtLmY2brg

def fav_groups():
		n = int(input())
		input()
		res = set(input().split())
		for _ in range(n - 1):
				input()
				res = res & set(input().split())
		print(len(res))
		print(*sorted(res))
	
if __name__ == '__main__':
		fav_groups()