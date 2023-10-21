import tkinter as tk
from docx import Document
import os
import shutil
from datetime import date

# Bu işlev, verileri txt dosyasından alır ve form alanlarına yansıtır
def load_data_from_txt():
    with open("siparis.txt", "r") as file:
        lines = file.readlines()

    veriler = {}
    for line in lines:
        key, value = line.strip().split(":")
        veriler[key] = value

    entry_ad.delete(0, tk.END)
    entry_ad.insert(0, veriler.get("ad", ""))
    entry_hikayeler.delete(0, tk.END)
    entry_hikayeler.insert(0, veriler.get("hikayeler", ""))
    entry_cinsiyet.delete(0, tk.END)
    entry_cinsiyet.insert(0, veriler.get("cinsiyet", ""))
    entry_tip.delete(0, tk.END)
    entry_tip.insert(0, veriler.get("tip", ""))

# Bu işlev, verileri form alanlarından alır ve belgeyi üretir
def generate_docs():
    ad = entry_ad.get()
    hikayeler = entry_hikayeler.get()
    cinsiyet = entry_cinsiyet.get()
    tip = entry_tip.get()

    hikaye_numaralari = hikayeler.split(',')
    hikaye_isimleri = ["hikaye-" + num for num in hikaye_numaralari]

    hikayalar_dizini = os.path.join("hikayeler", cinsiyet, tip)

    for hikaye_adi in hikaye_isimleri:
        original_path = os.path.join(hikayalar_dizini, hikaye_adi + ".docx")
        copy_path = os.path.join(hikayalar_dizini, hikaye_adi + "_" + ad + ".docx")
        shutil.copyfile(original_path, copy_path)

        word_replacements = [
            ("Xxixx", ad),
            ("Xxexx", ad + "ı")
        ]

        doc = Document(os.path.join(hikayalar_dizini, hikaye_adi + "_" + ad + ".docx"))

        for paragraph in doc.paragraphs:
            for search_word, replace_word in word_replacements:
                if search_word in paragraph.text:
                    for run in paragraph.runs:
                        run.text = run.text.replace(search_word, replace_word)

        doc.save(os.path.join("üretim", ad + "_" + hikaye_adi +"_"+tarih+ ".docx"))
        result_label.config(text="Belgeler başarıyla üretildi!")

    # Sipariş dosyasını taşı ve adını değiştir
    tarih = date.today().strftime("%Y-%m-%d")
    yeni_ad = ad+"-" + tarih + ".txt"
    shutil.move("siparis.txt", os.path.join("üretilmişler", yeni_ad))

# Tkinter penceresini oluştur
window = tk.Tk()
window.title("Belge Üretici")

# Verileri Yükle butonunu oluştur
load_button = tk.Button(window, text="Verileri Yükle", command=load_data_from_txt)

# Etiketler ve girdi alanları oluştur
label_ad = tk.Label(window, text="Ad:")
entry_ad = tk.Entry(window)
label_hikayeler = tk.Label(window, text="Hikayeler (Virgülle Ayırılmış):")
entry_hikayeler = tk.Entry(window)
label_cinsiyet = tk.Label(window, text="Cinsiyet:")
entry_cinsiyet = tk.Entry(window)
label_tip = tk.Label(window, text="Tip:")
entry_tip = tk.Entry(window)

# Üret butonunu oluştur
generate_button = tk.Button(window, text="Üret", command=generate_docs)

# Sonuç etiketi
result_label = tk.Label(window, text="")

# Arayüz öğelerini düzenle
load_button.grid(row=0, column=0, columnspan=2)
label_ad.grid(row=1, column=0)
entry_ad.grid(row=1, column=1)
label_hikayeler.grid(row=2, column=0)
entry_hikayeler.grid(row=2, column=1)
label_cinsiyet.grid(row=3, column=0)
entry_cinsiyet.grid(row=3, column=1)
label_tip.grid(row=4, column=0)
entry_tip.grid(row=4, column=1)
generate_button.grid(row=5, column=0, columnspan=2)
result_label.grid(row=6, column=0, columnspan=2)

window.mainloop()
