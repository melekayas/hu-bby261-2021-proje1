# ARAYÜZ DENEMESİ
from tkinter import *
from random import randint

pencere = Tk()
pencere.title('LOTO')
pencere.geometry('500x500')
pencere.configure(bg='red')


konu = Label(pencere, text="İşlenecek ders kodlamaları!..")
konu.config(font=("Arial", 12))
konu.pack()

def sayLoto():
    i = 0
    secilenler = [0, 0, 0, 0, 0, 0]
    for rastgele in secilenler:
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i += 1
        print(sorted(secilenler))
        i = 0

        numaralar = Label(pencere, text=secilenler)
        numaralar.pack()


goster = Button(pencere, text="Kodları Göster!..", command=sayLoto).grid(column=2, row=0)

cikis = Button(pencere, text="Çıkış yapınız.", command=pencere.quit).grid(column=0, row=0)


pencere.mainloop()





























