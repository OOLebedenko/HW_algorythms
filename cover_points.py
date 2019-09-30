def cover_poit(segments):
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
