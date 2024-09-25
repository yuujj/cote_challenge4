while True:
    n = int(input())
    if n == 0:
        break
    words = []

    for _ in range(n):
        word = input()
        words.append((word, word.lower()))

    print(sorted(words, key=lambda x: x[1])[0][0])