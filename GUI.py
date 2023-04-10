import tkinter as tk


def string_to_ascii(input_str):
    return [ord(c) for c in input_str]


def ascii_to_binary(ascii_list):
    return [bin(c)[2:].zfill(8) for c in ascii_list]


def ascii_to_decimal(ascii_list):
    return [c for c in ascii_list]


def ascii_to_hexadecimal(ascii_list):
    return [hex(c)[2:].zfill(2) for c in ascii_list]


def ascii_to_octal(ascii_list):
    return [oct(c)[2:].zfill(3) for c in ascii_list]


def convert():
    input_str = input_box.get()
    ascii_list = string_to_ascii(input_str)
    binary_list = ascii_to_binary(ascii_list)
    decimal_list = ascii_to_decimal(ascii_list)
    hexadecimal_list = ascii_to_hexadecimal(ascii_list)
    octal_list = ascii_to_octal(ascii_list)
    
    ascii_output.config(text=" ".join(map(str, ascii_list)))
    binary_output.config(text=" ".join(binary_list))
    decimal_output.config(text=" ".join(map(str, decimal_list)))
    hexadecimal_output.config(text=" ".join(hexadecimal_list))
    octal_output.config(text=" ".join(octal_list))

root = tk.Tk()
root.title("String Converter")
root['bg'] = "#FFA800"

# label dan texbox input
label_judul = tk.Label(root, text="Converter String to ASCII", font=("Arial", 16, "bold"), bg="#FFA800")
label_judul.place(relx=0.5, rely=0.1, anchor="center")

label1 = tk.Label(root, text="Masukkan String :", font=("Arial", 12), bg="#FFA800")
label1.place(relx=0.4, rely=0.15, anchor="center")

input_box = tk.Entry(root, width=30, font=("Poppins", 11), bd=3)
input_box.place(relx=0.5, rely=0.15, anchor="center", height=30)


# Tombol konversi
convert_button = tk.Button(root, text="Convert", command=convert, height=2, width=20, bg="#FF4141", bd=2)
convert_button.place(relx=0.61, rely=0.15, anchor="center", height=30)

label_hasil = tk.Label(root, text="Hasil Convert : ", font=("Helvetica", 15, "bold"), bg="#FFA800")
label_hasil.place(anchor="center", relx=0.065, rely=0.45)

#Output ASCII
ascii_label = tk.Label(root, text="ASCII = ",font=("Poppins", 12), bg="#FFA800")
ascii_label.place(relx=0.03, rely=0.5)
ascii_output = tk.Label(root, text="", font=("Poppins", 12), bg="#FFA800")
ascii_output.place(relx=0.062, rely=0.5)

#Output desimal
decimal_label = tk.Label(root, text="Decimal= ",font=("Poppins", 12), bg="#FFA800")
decimal_label.place(relx=0.03, rely=0.55)
decimal_output = tk.Label(root, text="", font=("Poppins", 12), bg="#FFA800")
decimal_output.place(relx=0.068, rely=0.55)

#Output hexadesimal
hexadecimal_label = tk.Label(root, text="Hexadecimal = ", font=("Poppins", 12), bg="#FFA800")
hexadecimal_label.place(relx=0.03, rely=0.6)
hexadecimal_output = tk.Label(root, text="", font=("Poppins", 12), bg="#FFA800")
hexadecimal_output.place(relx=0.088, rely=0.6)

#Ouput oktal
octal_label = tk.Label(root, text="Octal = ",font=("Poppins", 12), bg="#FFA800")
octal_label.place(relx=0.03, rely=0.65)
octal_output = tk.Label(root, text="", font=("Poppins", 12), bg="#FFA800")
octal_output.place(relx=0.06, rely=0.65)

#Output biner
binary_label = tk.Label(root, text="Binary = ",
                        font=("Poppins", 12), bg="#FFA800")
binary_label.place(relx=0.03, rely=0.7)
binary_output = tk.Label(root, text="", font=("Poppins", 12), bg="#FFA800")
binary_output.place(relx=0.064, rely=0.7)


root.mainloop()
