# Buatlah program untuk menampilkan angka 1 s/d n, dengan ketentuan: kelipatan 3 diganti “OK”, kelipatan 4 diganti “YES”, kelipatan 3 & 4 diganti “OKYES” Contoh output di bawah adalah ketika nilai “n” = 1

n = input('Enter n: ')
print('You Entered:', n)

for i in range(int(n)) :
    if (((i+1) % 3 == 0) and ((i+1) % 4 == 0)) : print("OKYES")
    elif (i+1) % 3 == 0 : print("OK")
    elif (i+1) % 4 == 0 : print("YES")
    else : print(i+1)