# 4 E. Нумерация дробей https://contest.yandex.ru/contest/59542/problems/E/
# решение за линейное время без использования бинпоиска

def main():

    import decimal

    decimal.getcontext().prec = 20
    D = decimal.Decimal


    n = int(input())
    diagonal = (((D(1) + D(8) * D(n)) ** D('0.5') - D(1)) / D(2))

    if int(diagonal) == diagonal:
        diagonal = int(diagonal)
        indexes = (diagonal, 1) if diagonal % 2 else (1, diagonal)
    else:
        diagonal = int(diagonal) + 1
        triangle_num = (diagonal ** 2 + diagonal) // 2
        indexes = ((diagonal - (triangle_num - n), 1 + (triangle_num - n)) if diagonal % 2
                  else (1 + (triangle_num - n), diagonal - (triangle_num - n)))

    print(f'{indexes[0]}/{indexes[1]}')

if __name__ == '__main__':
    main()      