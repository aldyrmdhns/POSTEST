#Bagian Menu
def menu():
    print('---------')
    print('Main Menu:')
    print('---------')
    print('1. USD')
    print('2. SGD')
    print('3. EUR')
    print('4. JPY')

def USD():
    HargaUSD = 14131
    rupiah = int(input("Masukkan Uang Rupiah anda = "))
    Hasil = rupiah / HargaUSD
    USD = round(Hasil, 2)
    print("Rp.",rupiah, "==>", USD, 'USD')

def SGD():
    HargaSGD = 10507
    rupiah = int(input("Masukkan Uang Rupiah anda = "))
    Hasil = rupiah / HargaSGD
    SGD = round(Hasil, 2)
    print("Rp.",rupiah, "==>", SGD, 'SGD')

def EUR():
    HargaEUR = 16428
    rupiah = int(input("Masukkan Uang Rupiah anda = "))
    Hasil = rupiah / HargaEUR
    EUR = round(Hasil, 2)
    print("Rp.",rupiah, "==>", EUR, 'EUR')

def JPY():
    HargaJPY = 123
    rupiah = int(input("Masukkan Uang Rupiah anda = "))
    Hasil = rupiah / HargaJPY
    JPY = round(Hasil, 2)
    print("Rp.",rupiah, "==>", JPY, 'JPY')

#Bagian Program Utama
print('Program Konversi Mata Uang Rupiah')
menu()
choice = input('masukan pilihan anda :')

if choice == '1':
    USD()
elif choice == '2':
    SGD()
elif choice == '3':
    EUR()
elif choice == '4':
    JPY()
else:
    print('error')
