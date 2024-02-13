import tkinter as tk
import time
import os

def open_files_and_write():
    files = ['file1.txt', 'file2.txt', 'file3.txt']  # Liste der Dateien

    for file_name in files:
        with open(file_name, 'w') as file:
            file.write("This is some text written in " + file_name)
        print("Text wurde in", file_name, "geschrieben.")

def close_files():
    files = ['file1.txt', 'file2.txt', 'file3.txt']

    for file_name in files:
        print("Datei", file_name, "wurde geschlossen.")
        time.sleep(1)  # Einen kurzen Moment warten, bevor die Datei geschlossen wird
        os.remove(file_name)  # Die Datei löschen

def cmatrix_animation():
    cmatrix = [
        "Wake up, Neo...",
        "The Matrix has you...",
        "Follow the white rabbit.",
        "Knock, knock, Neo.", 
        "Password: pass"
    ]

    while True:
        for line in cmatrix:
            print(line)
            time.sleep(0.2)  # Kurze Verzögerung zwischen den Zeilen
            os.system("cls" if os.name == "nt" else "clear")  # Bildschirm leeren (für Windows oder Unix)
            if input("Weiter? (ja/nein): ") != "ja":
                return

def main():
    # Öffnen und Schreiben von Dateien
    open_files_and_write()

    # GUI erstellen
    root = tk.Tk()
    root.title("Blinkende GUI")
    label = tk.Label(root, text="Dies ist eine blinkende GUI", font=("Helvetica", 16))
    label.pack()

    # Blinkender Effekt für die GUI
    while True:
        label.config(fg='red')
        root.update()
        time.sleep(0.5)
        label.config(fg='black')
        root.update()
        time.sleep(0.5)

    # Dateien schließen
    close_files()

    # cmatrix-Animation
    cmatrix_animation()

if __name__ == "__main__":
    main()
