"""
2.3 Условие. Задача на программирование: различные слагаемые

По данному числу 1≤n≤109 найдите максимальное число k,
для которого n можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых.
"""


def find_nonovelapping_terms(n):
    k = 1
    result = []
    while n > 2 * k:
        result.append(k)
        n -= k
        k += 1
    else:
        result.append(n)
    return result


if __name__ == "__main__":
    n = int(input())
    result = find_nonovelapping_terms(n)
    print(len(result))
    print(*result)
