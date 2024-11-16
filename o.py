import random
import os
class tebakAngka:
    def __init__( self ):
       angkaBenar = random.randrange(10)
       kesempatan = 0
       while True:
           os.system("cls")
           print("_____Tebak Angka_____")
           print("Kesempatan anda hanya 1x")
           print(f"Kesempatan anda serang : { kesempatan } ")
           angkajawab = int( input("Angka Tebakan Anda : ") )
           if angkajawab != angkaBenar and kesempatan == 1:
              print(f"LOSSER... Tebakan anda SALAH... {angkaBenar} ")
              break
           elif angkajawab < angkaBenar:
              print("Angka yg anda jawab lebih kecil dari angka tebakan")
              kesempatan += 1
           elif angkajawab > angkaBenar:
              print("Angka yg anda jawab lebih besar dari angka tebakan")
              kesempatan += 1
           elif angkaBenar == angkajawab:
              print("SELAMAT Anda adalah Pemenang")
              break
def main():
    run = tebakAngka()

if __name__ == "__main__":
    main()
print("Terima kasih telah menebak")