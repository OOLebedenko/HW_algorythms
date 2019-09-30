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
