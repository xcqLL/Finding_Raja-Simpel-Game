import os, sys
import time
import winsound
import pygame
from tkinter import messagebox

pygame.mixer.init()

def PlaySound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play() 

def StopSound():
    pygame.mixer.music.stop()        

def TypeEffect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.07)

def PlayTelephoneMusic():
    winsound.Beep(530, 1000)        

def Ending1():
    TypeEffect("\n\n Setelah killer turun kamu memutuskan mencari jalan keluar lain. dan kamu melihat telephone")
    TypeEffect("\n\n siapa yang akan kamu telpon?")
    TypeEffect("\n (1). Rian")
    TypeEffect("\n (2). Raja")
    TypeEffect("\n (3). Ibumu")
    TypeEffect("\n (4). Polisi")
    choice = int(input("\n\n Opsi apa yang anda pilih : "))

    if choice == 1:
        os.system("cls")
        TypeEffect("\n\n Kamu menelpon rian tapi tidak ada yang jawab dikarenakan killer sudah memotong kabel komunikasi telepon")
        Perbaikan_telepon()
    elif choice == 2:   
        os.system("cls")
        TypeEffect("\n\n Kamu menelpon raja tapi tidak ada yang jawab dikarenakan killer sudah memotong kabel komunikasi telepon")
        Perbaikan_telepon()
    elif choice == 3:   
        os.system("cls")
        TypeEffect("\n\n Kamu menelpon ibumu tapi tidak ada yang jawab dikarenakan killer sudah memotong kabel komunikasi telepon")
        Perbaikan_telepon()
    elif choice == 4:   
        os.system("cls")
        TypeEffect("\n\n Kamu menelpon polisi tapi tidak ada yang jawab dikarenakan killer sudah memotong kabel komunikasi telepon")
        Perbaikan_telepon()   

def Perbaikan_telepon():
    TypeEffect("\n\n Kamu pun memutuskan menyambungkan kabel telepon kembali.")
    time.sleep(2)
    TypeEffect("\n\n Tapi kamu tidak ada alat nya. kamu mencari alat untuk memperbaiki tsb sampai memasuki suatu ruangan disitu ada foto target siapa saja killer itu sudah bunuh")
    TypeEffect("\n\n Dan kamu melihat foto ibumu yang sudah di coret.")
    time.sleep(2)
    StopSound()
    os.system("cls")
    TypeEffect("\n\n Kamu melanjutkan mencari alat alat untuk memperbaiki tapi sialnya tepat kamu membuka pintu ada killer yang sedang mengasah pisau.")
    TypeEffect("\n\n Yang wajib membuatmu diam diam untuk melewatinya.")
    print("\n\n Press any bind to continue")
    os.system("Pause >nul")
    os.system("cls")
    PlaySound("silent.wav")   
    TypeEffect("\n\n Kamu lagi melewati killer dari belakang tapi kamu mmebutuhkan item yang ada di atas meja kanan, sedangkan killer lagi liat ke meja depan.")
    TypeEffect("\n\n Jadi kamu memutuskan mengambil barang secara diam diam. dan meracuni minuman dengan obat tidur")
    print("\n\n Press any bind to continue")
    os.system("Pause >nul")
    os.system("cls")
    TypeEffect("\n\n Kamu mendapatkan barang yang di maksud dan kamu berusaha kembali ke tempat semula.")
    TypeEffect("\n\n Selagi killer tertidur.")
    print("\n\n Press any bind to continue")
    os.system("Pause >nul")
    os.system("cls")
    StopSound()
    PlaySound("panic.wav") 
    TypeEffect("\n\n Well Well Well. not so fast")
    TypeEffect("\n\n Ketika kamu keluar kamu baru saja menginjak kayu yang rusak dimana itu bisa membuat step mu ketahuan dari bunyi tersebut")
    TypeEffect("\n\n Jadi...")
    os.system("cls")
    time.sleep(2)
    TypeEffect("\n\n Hal apa yang anda lakukan ketika di posisi tsb")
    TypeEffect("\n (1). Lari dan cari tempat sembunyi secepat mungkin")
    TypeEffect("\n (2). Diam di tempat sampai killer terbangun dan membunuh mu")
    TypeEffect("\n (3). Pasrah ama yang maha kuasa")
    choice = int(input("\n\n Opsi apa yang anda pilih : "))

    if choice == 1:
        os.system("cls")
        TypeEffect("\n\n Dikarenakan kamu lari , kamu membuat suara yang keras yang membuat killer itu terbangun dan mengejar mu")
        TypeEffect("\n\n Disaat kamu panik tidak bisa tenang hal apa yang akan kamu lakukan") 
        TypeEffect("\n (1). Masuk ke tempat yang ada zat asam")
        TypeEffect("\n (2). Naik ke lantai 2")
        TypeEffect("\n (3). Masuk ke bawah kasur")
        choice = int(input("\n\n Opsi apa yang anda pilih : "))

        if choice == 1:
            os.system("cls")
            TypeEffect("\n\n Kamu memasuki ruangan yang ada zat asam nya sampai terkena di kepala mu")   
            TypeEffect("\n\n Better luck next time")
            time.sleep(1)
            sys.exit()
        elif choice == 2:
            os.system("cls")
            TypeEffect("\n\n Kamu mengulangi kebodohan mu sebanyak 2x")   
            TypeEffect("\n\n Better luck next time")
            time.sleep(1)
            sys.exit()

        elif choice == 3:
            StopSound()
            os.system("cls")
            TypeEffect("\n\n Kamu bersembunyi di bawah kasur sampai keadaan benar benar aman")   
            TypeEffect("\n\n Setelah killer melewati kamu, killer berkeliaran di setiap tempat, yang membuatmu kesusahan untuk mencapai tempat telephone")
            print("\n\n Press any bind to continue")
            os.system("Pause >nul")
            TypeEffect("\n\n Dikarenakan itu kamu memutuskan kembali ketempat awal")
            os.system("cls")
            tamat() 

        
    elif choice == 2:   
        os.system("cls")   
        TypeEffect("\n\n Kamu menunggu killer bangun dan membunuh mu")   
        TypeEffect("\n\n Sama saja walaupun kamu langsung lari karena kamu panik kamu mati di trow knife")   
        time.sleep(2)
        messagebox.showinfo("Calm", "ENDING 4 : PANIC", icon = "info", parent = None)

        TypeEffect("\n\n Dev : smth oppenheimer")
        TypeEffect("\n\n Source code (Github) : https://github.com/xcqLL")

        print("\n\n Press any bind to continue")
        os.system("Pause >nul")

    elif choice == 3:   
        os.system("cls")   
        TypeEffect("\n\n Kamu pasrah ama tuhan, dan kamu mati terbunuh di tempat")   
        time.sleep(2)
        messagebox.showinfo("Pasrah", "ENDING 5 : beliau ini kocak gemink", icon = "info", parent = None)

        TypeEffect("\n\n Dev : smth oppenheimer")
        TypeEffect("\n\n Source code (Github) : https://github.com/xcqLL")

        print("\n\n Press any bind to continue")
        os.system("Pause >nul")

def tamat():
    TypeEffect("\n\n Kamu pun memutuskan menyambungkan kabel telepon kembali.")
    TypeEffect("\n\n Setelah kamu kembali kamu memperbaiki telepon itu dan")
    TypeEffect("\n\n siapa yang akan kamu telpon?")
    TypeEffect("\n (1). Rian")
    TypeEffect("\n (2). Raja")
    TypeEffect("\n (3). Ibumu")
    TypeEffect("\n (4). Polisi")
    choice = int(input("\n\n Opsi apa yang anda pilih : "))

    if choice == 1:
        PlayTelephoneMusic()
        os.system("cls")
        TypeEffect("\n\n Kamu menelpon rian tapi dia menjawab 'Lu udah nemu anak gw si raja ? kalo udah bilang ya entar gw tf 1M' ")
        print("\n\n Press any bind to continue")
        os.system("Pause >nul")
        os.system("cls")
        tamat()

    elif choice == 2:   
        PlayTelephoneMusic()
        os.system("cls")
        TypeEffect("\n\n Kamu menelpon raja tapi tidak ada yang jawab")
        print("\n\n Press any bind to continue")
        os.system("Pause >nul")
        os.system("cls")
        tamat()

    elif choice == 3:   
        PlayTelephoneMusic()
        os.system("cls")
        TypeEffect("\n\n Kamu menelpon ibumu tapi tidak ada yang jawab")
        print("\n\n Press any bind to continue")
        os.system("Pause >nul")
        os.system("cls")
        tamat()

    elif choice == 4:   
        PlayTelephoneMusic()
        os.system("cls")
        TypeEffect("\n\n Kamu menelpon polisi tapi, butuh waktu 1 jam, polisi mencari keberadaan mu sampai akhirnya ketemu bahwa kamu tersesat di hutan")
        TypeEffect("\n\n Tapi sialnya killer dengan skill aimbot nya malempar knife ke kamu dan terkena di punggung")
        print("\n\n Press any bind to continue")
        os.system("Pause >nul")
        TypeEffect("\n\n Dan kamu di kejar. kamu pun berusaha lari sampai akhirnya terjatuh")
        os.system("cls")
        TypeEffect("\n\n Disaat kamu terjatuh kamu melihat deagel di bawah meja dan mengambil nya dan menembakan di kepala killer tsb")
        TypeEffect("\n\n Sampai polisi tiba . kamu di tuduh pembunuhan dan killer aslinya adalah kamu dan kamu di jatuhi hukuman mati")
        os.system("cls")
        PlaySound("ending1.wav")   
        TypeEffect("\n\n the end")
        messagebox.showinfo("Bravo", "ENDING 1 : TRUE ENDING", icon = "info", parent = None)

        TypeEffect("\n\n Dev : smth oppenheimer")
        TypeEffect("\n\n Source code (Github) : https://github.com/xcqLL")
        

        print("\n\n Press any bind to continue")
        os.system("Pause >nul")
