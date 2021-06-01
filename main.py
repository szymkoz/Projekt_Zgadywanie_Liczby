import tkinter as tk
import random

window = tk.Tk()
window.geometry("500x500")

wylosowana = None


def wylosuj():
    global wylosowana
    wylosowana = random.randrange(0, int(pole_maks.get()) + 1)
    tekst_wiadomosc.config(text="Zgadnij w polu poniżej:")


def zgadnij():
    if int(pole_zgadnieta.get()) == wylosowana:
        tekst_wiadomosc.config(text="Super! Updało się, zgadłeś!")
    else:
        tekst_wiadomosc.config(text="Nie zgadłeś :(")


tekst_zakres = tk.Label(text="Zakres losowanych liczb - od 0 do:")
tekst_zakres.pack()

pole_maks = tk.Entry()
pole_maks.pack()

przycisk_losuj = tk.Button(text="Losuj!", command=wylosuj)
przycisk_losuj.pack()

tekst_wiadomosc = tk.Label()
tekst_wiadomosc.pack()

pole_zgadnieta = tk.Entry()
pole_zgadnieta.pack()

przycisk_zamknij = tk.Button(text="Zgadnij", command=zgadnij)
przycisk_zamknij.pack()


window.mainloop()
