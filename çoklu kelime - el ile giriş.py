import tkinter as tk
from docx import Document
import os
import shutil

# Bu işlev, üret butonuna tıklandığında çalışır
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

        doc.save(os.path.join("üretim", hikaye_adi + "_" + ad + ".docx"))
        result_label.config(text="Belgeler başarıyla üretildi!")

# Tkinter penceresini oluştur
window = tk.Tk()
window.title("Belge Üretici")

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
label_ad.grid(row=0, column=0)
entry_ad.grid(row=0, column=1)
label_hikayeler.grid(row=1, column=0)
entry_hikayeler.grid(row=1, column=1)
label_cinsiyet.grid(row=2, column=0)
entry_cinsiyet.grid(row=2, column=1)
label_tip.grid(row=3, column=0)
entry_tip.grid(row=3, column=1)
generate_button.grid(row=4, column=0, columnspan=2)
result_label.grid(row=5, column=0, columnspan=2)

window.mainloop()
