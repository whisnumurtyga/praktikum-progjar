def luas(r) :
    print("luas: ", 3.14 * r * r)

def keliling(r) :
    print("keliling: ", 2 * 3.14 * r)


while True : 
    print("\n\n\n1. Luas Lingkaran \n2. Keliling Lingkaran : \n3. Exit")
    select = input("pilih menu: ")
    if int(select) == 3 :
        break
    else :
        r = input("masukkan jari-jari: ")
        if int(select) == 1 : 
            luas(int(r))
        elif int(select) == 2 : 
            keliling(int(r))


print("after while")

