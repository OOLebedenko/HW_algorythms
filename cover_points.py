"""
2.1 Условие. Задача на программирование: покрыть отрезки точками

По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤109,
задающих начало и конец отрезка.
Выведите оптимальное число m точек и сами m точек.
Если таких множеств точек несколько, выведите любое из них.
"""


def cover_points(segments):
    ans = []
    segments.sort(key=lambda x: x[1])
    current_y = None
    for x, y in segments:
        if current_y is None:
            current_y = y
        if current_y >= x:
            continue
        else:
            ans.append(current_y)
            current_y = y
    ans.append(current_y)
    return ans


if __name__ == "__main__":
    k = int(input())
    segments = [list(map(int, input().split())) for _ in range(k)]
    ans = cover_poit(segments)
    print(len(ans))
    print(" ".join(map(str, ans)))
