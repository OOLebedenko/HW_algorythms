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
