def menu():
    print('Konversi Bilangan')
    print('1. Decimal')
    print('2. Hexadecimal')
    print('3. Oktal')
    print('4. Biner')
    print('5. Exit')
    angka = input('Pilih Menu : ')
    if angka == '1':
        decimal()
    elif angka == '2':
        hexadecimal()
    elif angka == '3':
        oktal()
    elif angka == '4':
        biner()
    elif angka == '5':
        exit()
    else:
        tdkada()

def tdkada():
    tdkada = input("Menu Tidak Ada! tekan ENTER untuk kembali")
    menu()

def decimal():
    print("konversi Bilangan Decimal")
    try:
        nilai = int(input("Masukkan bilangan decimal : "))
    except ValueError:
        error = input ("Mohon masukkan angka [Tekan apapun untuk lanjut]")
        decimal()
    bineri = bin(nilai).replace("0b","")
    oktal = oct(nilai).replace("0o","")
    heks = hex(nilai).replace("0x","")
    
    print('Biner       : ',bineri)
    print('Oktal       : ',oktal)
    print('Hexadecimal : ',heks)
    pilihan()
    
def hexadecimal():
    print("konversi Bilangan Hexadecimal")
    try:
        nilai = int(input("Masukkan bilangan hexadecimal : ",16))
    except ValueError:
        error = input ("Mohon masukkan angka [Tekan apapun untuk lanjut]")
        hexadecimal()
    biner = bin(nilai).replace("0b","")
    oktal = oct(nilai).replace("0o","")

    print('Biner   : ',biner)
    print('Oktal   : ',oktal)
    print('Decimal : ',nilai)
    pilihan()
    
def oktal():
    print("konversi bilangan Oktal")
    try:
        nilai = int(input("Masukkan bilangan oktal : "),8)
    except ValueError:
        error = input ("Mohon masukkan angka [Tekan apapun untuk lanjut]")
        oktal()
    biner = bin(nilai).replace("0b","")
    heks = hex(nilai).replace("0x","")

    print('Biner       : ',biner)
    print('Decimal     : ',nilai)
    print('Hexadecimal : ',heks)
    pilihan()
    

def biner():
    print("konversi Bilangan Biner")
    try:
        nilai = int(input("Masukkan bilangan biner : "),2)
    except ValueError:
        error = input ("Mohon masukkan angka [Tekan apapun untuk lanjut]")
        biner()
    oktal = oct(nilai).replace("0o","")
    heks = hex(nilai).replace("0x","")

    print('Oktal       : ',oktal)
    print('Decimal     : ',nilai)
    print('Hexadecimal : ',heks)
    pilihan()

    
def pilihan():
    pilih = input('Ingin mengonversi bilangan lain? ( y / t ) :')
    if pilih == "y" or pilih == "Y":
        menu()
    elif pilih == "t" or pilih == "T":
        exit()
    else:
        salah()
        
def salah():
    pilihs = input('Mohon pilih y/Y untuk pergi ke menu dan pilih t/T untuk keluar :')
    if pilihs == "y" or pilihs == "Y":
        menu()
    elif pilihs == "t" or pilihs == "T":
        exit()
    else:
        salah()
        
menu()
