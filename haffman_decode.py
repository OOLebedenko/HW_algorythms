def haffman_decode(encoded, code):
    decoded = ""
    while encoded:
        for ch, acc in code.items():
            if encoded.startswith(acc):
                decoded += ch
                encoded = encoded[len(acc):]
    return (decoded)


def main():
    k, l = map(int, (input().split()))
    d = [tuple(input().split(":")) for _ in range(k)]
    code = {ch: key.strip() for ch, key in d}
    encoded = input()
    decoded = haffman_decode(encoded, code)
    print(decoded)


if __name__ == "__main__":
    main()
