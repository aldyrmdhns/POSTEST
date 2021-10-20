#Sistem Login
username = 'aldyrmdhns'
password = '2882'

def login (user_name, pass_word) :
    if user_name == username and pass_word == password :
        hasil = True
    else :
        hasil = False

    return hasil

#Menu
def menu():
    print('Pilihan Menu :')
    print('--------------')
    print('1. profil')
    print('2. mata kuliah')

def profil():
    bio = {
        'Nama' : 'Aldy Ramadhan Syahputra',
        'NIM' : 2109106079,
        'Kelas' : 'B',
        'Angkatan' : 2021,
        'Jenis Kelamin' : 'Laki-Laki',
        'status' : 'single'
    }
    for key, value in bio.items():
        print(key, ':', value)

def mata_kuliah():
    matkul = ['APD', 'FisDas', 'Kalkulus', 'Logika Informatika', 'PTI']
    jumlah_matkul = len(matkul)
    print('Jumlah matkul yang anda ambil adalah', jumlah_matkul, ':')
    for matkul_items in matkul:
        print(matkul_items)

#Program Utama
print('selamat datang!')
print('---------------')
i=3
while i>=1:
    user_name=input("masukan username anda :")
    pass_word=input("masukan password :")
    hasil=(login(user_name, pass_word))
    
    if hasil == True :
        print ("login user berhasil")
        menu()
        choice = (input('Silahkan dipilih :'))
        if choice == '1':
            profil()
            break
        elif choice =='2':
            mata_kuliah()
            break
        else:
            print('error')
            break      
    elif hasil == False :
        i-=1
        print("gagal login, sisa percobaan login adalah :", i )

