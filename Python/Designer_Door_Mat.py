if __name__ == '__main__':
  n, m = map(int, input().split())
  if n % 2 == 1 and m == n * 3:
    a = ".|."
    for i in range(0, n // 2, 1):
      print(a.center((m),'-'))
      a = a + ".|..|."

    print("WELCOME".center((m),'-'))
    f = n - 2
    for i in range(n // 2, 0, -1):
      print((f * ".|." ).center((m),'-'))
      f = f - 2
