def f(x: int) -> int:
    print(x)
    x *= 2
    return x

y: int = f(3)

print(y)