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

def Ending2():   
    PlaySound("silent.wav")
    TypeEffect("\n\n Kamu terbangun di basement dan di seret killer ke ruangan penyiksaan .Disitu kamu bertemu orang random ya itu ibumu sendiri")
    TypeEffect("\n\n Ketika si killer ingin mengambil asam dan alat tajam") 
    os.system("cls")
    time.sleep(2)
    TypeEffect("\n\n Kamu bingung mau ngapain sampai kamu memutuskan menggunakan cari trsbt")
    TypeEffect("\n (1). Menggunakan krematorium untuk membakar tali")
    TypeEffect("\n (2). Menggunakan kaki ibumu untuk melepaskan tali di tangan")
    TypeEffect("\n (3). BY ONE DEK AMA KILLER")
    choice = int(input("\n\n Opsi apa yang anda pilih : "))

    if choice == 1:
        os.system("cls")
        TypeEffect("\n\n Kamu berhasil melepas tali tapi kamu terbakar habis")
        time.sleep(2)
        os.system("cls")
        TypeEffect("\n\n Better luck next time")
        time.sleep(1)
        sys.exit()
    elif choice == 2:
            os.system("cls")
            TypeEffect("\n\n Ibumu membantumu melepaskan tali di tangan dengan kaki dan di atas meja ada beberapa senjata/barang tajam untuk kamu gunakan")
            TypeEffect("\n\n pilih 2 item tersbt untuk face to face sama killer")
            TypeEffect("\n (1). Pisau dapur dan tali")
            TypeEffect("\n (2). Molotov dan Pisau")
            TypeEffect("\n (3). Tangan kosong")
            choice = int(input("\n\n Opsi apa yang anda pilih : "))

            if choice == 1:
                StopSound()
                os.system("cls")
                TypeEffect("\n\n Kamu pun mati terbunuh :)")
                time.sleep(2)
                os.system("cls")
                TypeEffect("\n\n Better luck next time")
                time.sleep(1)
                sys.exit()
            elif choice == 2:
                StopSound()
                os.system("cls")
                TypeEffect("\n\n Dengan pede nya lu nge bunuh si killer edngan molotov dan pisau")
                TypeEffect("\n\n Ketika si killer terbakar dikarenakan molotov kamu menggunakan pisau untuk menusuknya dan membuka topengnya")
                os.system("cls")
                TypeEffect("\n\n Ternyata itu adalah raja. anak yang menghilang 4 tahun setelah kabur dari rumah di karenakan tiap main valorant di suruh matikan bapaknya")
                os.system("cls")
                PlaySound("ending1.wav")   
                TypeEffect("\n\n the end")
                messagebox.showinfo("Bravo", "ENDING 2 : DEAD ENDING", icon = "info", parent = None)

                TypeEffect("\n\n Dev : smth oppenheimer")
                TypeEffect("\n\n Source code (Github) : https://github.com/xcqLL")
        

                print("\n\n Press any bind to continue")
                os.system("Pause >nul")
                sys.exit()
            elif choice == 3:  
                StopSound()
                os.system("cls")
                TypeEffect("\n\n Kamu pun mati terbunuh :)")
                time.sleep(2)
  

    elif choice == 3:
            os.system("cls")
            TypeEffect("\n\n Kamu pun mati terbunuh :)")
            time.sleep(2)
            os.system("cls")
            TypeEffect("\n\n Better luck next time")
            time.sleep(1)
            sys.exit()