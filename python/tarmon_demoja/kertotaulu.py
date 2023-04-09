def kertotaulu():
    user_input = int(input("Choose a number"))
    for i in range(11):
        print("{} x {} = {}". format(i, user_input, i * user_input))


def main():
    kertotaulu()


if __name__ == "__main__":
    main()