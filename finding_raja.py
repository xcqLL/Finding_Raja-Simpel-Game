import os
import pygame
from game import Game
import time
import winsound
from tkinter import messagebox

pygame.mixer.init()

def TypeEffect(text):
    for char in text:
        winsound.Beep(530, 500)
        print(char, end='', flush=True)
        time.sleep(0.07)

def PlaySound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def StopSound():
    pygame.mixer.music.stop()

cmd = 'mode 1920,1080' # W / H
os.system(cmd)    

def main():
    PlaySound("menu.wav")
    
    print("[1] Start game")
    print("[2] Exit ")
    choice = int(input("Enter your choice: "))

    if choice == 1: 
        os.system("cls")
        print("\n\n")
        TypeEffect("   Starting the game...")
        StopSound()
        os.system("cls")
        Game()
    elif choice == 2:
        messagebox.showinfo("TOLOL", "CULUN AMAT LU KONTOL MASAK KELUAR ?", icon = "warning", parent = None)
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()