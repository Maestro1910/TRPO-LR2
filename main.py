from calc import __version__, add, div, mul, sub


def main():
    print(f"Calc v{__version__}")
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", sub(7, 4))
    print("6 * 7 =", mul(6, 7))
    print("10 / 4 =", div(10, 4))


if __name__ == "__main__":
    main()
