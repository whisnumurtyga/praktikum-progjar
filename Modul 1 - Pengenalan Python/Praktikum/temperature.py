def farToCel(r) :
    print("luas: ", 3.14 * r * r)

def celToFar(r) :
    print("keliling: ", 2 * 3.14 * r)


while True : 
    print("\n\n\n1. Celcius ke Farenheit \n2. Farenheit ke Celcius : \n3. Exit")
    select = input("pilih menu: ")
    if int(select) == 3 :
        break
    else :
        r = input("masukkan suhu: ")
        if int(select) == 1 : 
            luas(int(r))
        elif int(select) == 2 : 
            keliling(int(r))


print("after while")

