def main ():
     # asks and saves a mass
     m = input("m: ")
     print(energy(m))


def energy(m):
    e = int(m) * pow(300000000, 2)
    return e

main()
    






