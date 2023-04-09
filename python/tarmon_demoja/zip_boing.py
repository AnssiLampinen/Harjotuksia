


def zip_boing():
    """
    Jos jaollinen x -> zip
    Jos jaollinen y -> boing
    Jos jaollinen x ja y -> zipboing
    """
    x = 3
    y = 7
    z = 100 #Viimeinen tutkittava numero
    i = 1
    while i <= z:
        a = i%x
        b = i%y
        if a == 0 and b == 0:
            print("zipboing")
        elif a == 0:
            print("zip")
        elif b == 0:
            print("Boing")
        else:
            print(i)
        i += 1


def zip_boing2(x, y, z):
    for i in range(1, z + 1):
        a = i%x
        b = i%y
        if a == 0 and b == 0:
            print("zipboing")
        elif a == 0:
            print("zip")
        elif b == 0:
            print("Boing")
        else:
            print(i)


def main():
    zip_boing2(3, 7, 100)


if __name__ == "__main__":
    main()

