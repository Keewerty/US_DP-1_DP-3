import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("Aplikasi Sederhana Tkinter")
root.geometry = ("1920 x 700")

def string_to_hex(s):
    hex_string = ""
    for c in s:
        hex_val = hex(ord(c))[2:]  # remove the '0x' prefix
        hex_string += hex_val
    return hex_string

def string_to_decimal(s):
    decimal_string = ""
    for c in s:
        decimal_val = str(ord(c))
        decimal_string += decimal_val
    return decimal_string

def string_to_binary(s):
    binary_string = ""
    for c in s:
        binary_val = bin(ord(c))[2:]  # remove the '0b' prefix
        # pad with leading zeros so each binary value has 8 digits
        binary_val = binary_val.rjust(8, '0')
        binary_string += binary_val
    return binary_string

def string_to_octal(s):
    octal_string = ""
    for c in s:
        octal_val = oct(ord(c))[2:]  # remove the '0o' prefix
        # pad with leading zeros so each octal value has 3 digits
        octal_val = octal_val.rjust(3, '0')
        octal_string += octal_val
    return octal_string

def menu():
    s = input("Masukkan kata : ")
    hex_string = string_to_hex(s)
    print("Nilai Hexadecimal :", hex_string)
    decimal_string = string_to_decimal(s)
    print("Nilai Decimal :", decimal_string)
    binary_string = string_to_binary(s)
    print("Nilai Binary :", binary_string)
    octal_string = string_to_octal(s)
    print("Nilai Octal :", octal_string)
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
root.mainloop()