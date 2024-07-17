# 3 E. Два из трех https://contest.yandex.ru/contest/59541/problems/E/?success=113653996#30404/2022_08_30/wjAMfuJsIo

def main():
    input()
    a = set(map(int, input().split()))
    input()
    b = set(map(int, input().split()))
    input()
    c = set(map(int, input().split()))
    print(*sorted(a&b|a&c|c&b-a&b&c))

if __name__ == '__main__':
    main()  