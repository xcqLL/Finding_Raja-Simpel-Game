import os
import time, sys
import winsound
import pygame
from tkinter import messagebox
from ending1 import Ending1
from ending2 import Ending2
import subprocess

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

def Game():
    PlaySound("rain.wav")
    TypeEffect("\n\n Jadi ada sebuah anak yang bernama edvan dia tersesat di hutan, dan melihat rumah tua berlantai 2")
    print("\n\n Press any bind to continue")
    os.system("Pause >nul")
    os.system("cls")

    TypeEffect("\n\n Karena ini hujan dan kamu tidak ada perlengkapan apa apa hal apa yang akan kamu lakukan?")
    print("\n\nINGAT ! .Pilihan ini memengaruhi 6 ending")
    TypeEffect("\n (1). memasuki rumah tersebut dan beristirahat sejenak sampai hujan reda")
    TypeEffect("\n (2). kamu tidak memutuskan memasuki rumah tsb dan memutuskan untuk melanjutkan perjalanan walaupun kehujanan")
    choice = int(input("\n\n Opsi apa yang anda pilih : "))

    if choice == 1:
        StopSound()
        os.system("cls")
        TypeEffect("\n\n Edvan memasuki rumah tersebut tapi malah terkunci dan . . . .")
        PlaySound("scream.wav")
        time.sleep(6)
        os.system("cls")
        PlaySound("panic.wav")
        TypeEffect("\n\n .....")
        os.system("cls")
        TypeEffect("\n\n YOU NEED TO HIDE")
        TypeEffect("\n (1). Masuk ke dalam Lemari")
        TypeEffect("\n (2). Lari keluar rumah")
        TypeEffect("\n (3). Lari turun ke basement")
        TypeEffect("\n (4). Lari naik ke atas tangga")
        choice = int(input("\n\n Opsi apa yang anda pilih : "))

        if choice == 1:
            os.system("cls")
            TypeEffect("\n\n Killer bertopeng dan membawa golok datang mencari mu tapi kamu menghilang")
            time.sleep(2)
            TypeEffect("\n\n Dan killer melewati kamu tanpa sepengetahuan dia. diapun melanjutkan memutilasi korban sebelumnya di basement")
            Ending1()
        elif choice == 2: 
            os.system("cls")
            TypeEffect("\n\n Sayangnya. pintu keluar sudah tertutup")
            time.sleep(2)
            os.system("cls")
            TypeEffect("\n\n Dan kamu pun mati karena. Killer sudah mendengar bahwa ada orang lain yang masuk rumah tersebut")
            TypeEffect("\n\n Better luck next time")
            time.sleep(1)
            sys.exit()

        elif choice == 3:
            os.system("cls")
            TypeEffect("\n\n Kamu pun turun ke basement karena panik. dan mati karena bertemu killer :)")
            time.sleep(2)
            os.system("cls")
            TypeEffect("\n\n Kenapa ?. dikarenakan killer barusaja dari bawah basement naik ke atas")
            TypeEffect("\n\n Better luck next time")
            time.sleep(1)
            sys.exit()

        elif choice == 4:  
            os.system("cls")  
            TypeEffect("\n\n tangga yang kamu naiki ternyata rusak dan membuat mu jatuh")
            time.sleep(2)
            os.system("cls")
            TypeEffect("\n\n tetapi kamu malah terjatuh ke ruang basement")
            os.system("cls")
            Ending2()

    if choice == 2: 
        PlaySound("rain.wav")   
        os.system("cls")   
        TypeEffect("\n\n Ditengah hujan yang deras bukannya masuk rumah tsb malah memutuskan melanjutkan perjalanan dan akhirnya kamu mati di tengah hutan")   
        TypeEffect("\n\n Kamu telah melakukan perjalanan sebanyak 2 KM di saat hujan deras")   
        time.sleep(2)
        messagebox.showinfo("Bravo", "ENDING 3 : LEBIH BAIK MATI DALAM KEADAAN DI BUNUH/SHOLAT/TENGGELAM DARI PADA SAMA HUJAN. DONGO PISAN", icon = "info", parent = None)
        