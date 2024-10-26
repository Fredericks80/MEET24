# FUNCITION = Statement yang berisi tugas / task tertentu dan dapat digunakan berulang - ulang kali...
def hello():
    print("HEII KELAS CODING...")
    print("CODING ITU MUDAH !")
def batas():
    print("-"*30)
hello()
hello()

batas()

def namaGue(nama):
    print(f"heiiii nama gue adalah {nama}, saya ganteng sekali !")

namaGue("selo")
namaGue("mario")
batas()

def biodata(nama, umur, alamat, citacita):
    print(f"Hai nama saya { nama } sekarang ber umur { umur } tahun, alamat di { alamat } dan bercita-cita sebagai { citacita }")

biodata("kenzo",15,"Plg","Pilot")

batas()

def gayaBerat(m, g):
    print(f"Berat gaya (F) = {m*g}N")

m = int(input("Enter Massa Benda ="))
g = int(input("Enter Gravitasi Bumi ="))
gayaBerat(m, g)

batas()
def aritmatika(a,b):
    hasil_tambah = a+b
    return hasil_tambah
hasil = aritmatika( 6, 8 )
print(f"1 Hasilnya = {hasil}")
print(f"2 Hasilnya = { aritmatika( 9, 6 ) }")

batas()
def gayaBerat2( m, g ):
    return ( m * g )

print(f"Hasil nilai gaya berat = { gayaBerat2( 10, 5 )} N")
print(f"gaya berat = { gayaBerat2( 5, 57 )} N")

batas()
def temanKu(data):
    datas = data.copy()
    for i in datas:
        print(f"temanku adalah : {i}")
dataList = [ "niel", "mario", "erik", "azam" ]
temanKu(dataList)
batas()
def aritmatikaKu( a,b ):
    hasil_tambah = a + b
    hasil_kurang = a - b
    hasil_kali = a * b
    hasil_bagi = a / b
    hasil_mod = a & b
    return hasil_tambah, hasil_kurang, hasil_kali, hasil_bagi, hasil_mod
print(f"hasil = { aritmatikaKu( 20, 5)}")
h_tambah, h_kurang, h_kali, h_bagi, h_mod = aritmatikaKu( 20,  5 )
print(f"Hasil 1 : { h_tambah }")