"""
2.2 Условие. Задача на программирование: непрерывный рюкзак

Первая строка содержит количество предметов 1≤n≤103 и вместимость рюкзака 0≤W≤2⋅106.
Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅106 и объём 0<wi≤2⋅106 предмета (n, W, ci, wi — целые числа).
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
"""


def continuous_backpack(capacity, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    full_price = 0
    for price, weight in items:
        current_capacity = capacity - weight
        if current_capacity >= 0:
            capacity -= weight
            full_price += price
        elif current_capacity < 0:
            full_price += price * capacity / weight
            break
    return full_price


if __name__ == "__main__":
    k, capacity = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(k)]
    print(continuous_backpack(capacity, items))
