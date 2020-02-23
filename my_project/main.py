from module import add, even, hello


def main():
    li = [i for i in range(add(4))]
    print(hello(f"Python {even(li)[2]}"))


if __name__ == "__main__":
    main()
