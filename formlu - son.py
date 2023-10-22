import tkinter as tk
from docx import Document
import os
import shutil
from datetime import date

def ihalii(kelime):
    kelime = kelime.lower()
    harfler = ""
    ek = ""
    son_harf = kelime[-1]
    son_iki_harf = kelime[-2] if len(kelime) >= 2 else ""

    

    if son_harf in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "s"
    elif son_iki_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"] and son_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "zz"
    else:
        harfler = "z"

    if harfler == 'zz':
        onceki_harf = kelime[-3] if len(kelime) >= 3 else ""
        if onceki_harf in ["a", "ı"]:
            ek = 'ı'
        elif onceki_harf in ["e", "i"]:
            ek = 'i'
        elif onceki_harf in ["o", "u"]:
            ek = 'u'
        elif onceki_harf in ["ö", "ü"]:
            ek = 'ü'
    elif harfler == 'z':
        onceki_harf = kelime[-2]
        if onceki_harf in ["a", "ı"]:
            ek = 'ı'
        elif onceki_harf in ["e", "i"]:
            ek = 'i'
        elif onceki_harf in ["o", "u"]:
            ek = 'u'
        elif onceki_harf in ["ö", "ü"]:
            ek = 'ü'
    elif harfler == 's':
        if son_harf in ["a", "ı"]:
            ek = 'yı'
        elif son_harf in ["e", "i"]:
            ek = 'yi'
        elif son_harf in ["o", "u"]:
            ek = 'yu'
        elif son_harf in ["ö", "ü"]:
            ek = 'yü'

    return f"{kelime}'{ek}"

def ehalii(kelime):
    kelime = kelime.lower()
    harfler = ""
    ek = ""
    son_harf = kelime[-1]
    son_iki_harf = kelime[-2] if len(kelime) >= 2 else ""

    print(f"{son_harf}\n")

    if son_harf in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "s"
    elif son_iki_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"] and son_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "zz"
    else:
        harfler = "z"

    if harfler == 'zz':
        onceki_harf = kelime[-3] if len(kelime) >= 3 else ""
        if onceki_harf in ["a", "ı", "o", "u"]:
            ek = 'a'
        elif onceki_harf in ["e", "i", "ö", "ü"]:
            ek = 'e'
    elif harfler == 'z':
        onceki_harf = kelime[-2]
        if onceki_harf in ["a", "ı", "o", "u"]:
            ek = 'a'
        elif onceki_harf in ["e", "i", "ö", "ü"]:
            ek = 'e'
    elif harfler == 's':
        if son_harf in ["a", "ı", "o", "u"]:
            ek = 'ya'
        elif son_harf in ["e", "i", "ö", "ü"]:
            ek = 'ye'

    return f"{kelime}'{ek}"


def dehalii(kelime):
    kelime = kelime.lower()
    harfler = ""
    ek = ""
    son_harf = kelime[-1]
    son_iki_harf = kelime[-2] if len(kelime) >= 2 else ""

    print(f"{son_harf}\n")

    if son_harf in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "s"
    elif son_iki_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"] and son_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "zz"
    else:
        harfler = "z"

    if harfler == 'zz':
        onceki_harf = kelime[-3] if len(kelime) >= 3 else ""
        if onceki_harf in ["a", "ı", "o", "u"]:
            ek = 'da'
        elif onceki_harf in ["e", "i", "ö", "ü"]:
            ek = 'de'
    elif harfler == 'z':
        onceki_harf = kelime[-2]
        if onceki_harf in ["a", "ı", "o", "u"]:
            ek = 'da'
        elif onceki_harf in ["e", "i", "ö", "ü"]:
            ek = 'de'
    elif harfler == 's':
        if son_harf in ["a", "ı", "o", "u"]:
            ek = 'da'
        elif son_harf in ["e", "i", "ö", "ü"]:
            ek = 'de'

    return f"{kelime}'{ek}"

def denhalii(kelime):
    kelime = kelime.lower()
    harfler = ""
    ek = ""
    son_harf = kelime[-1]
    son_iki_harf = kelime[-2] if len(kelime) >= 2 else ""

    print(f"{son_harf}\n")

    if son_harf in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "s"
    elif son_iki_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"] and son_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "zz"
    else:
        harfler = "z"

    if harfler == 'zz':
        onceki_harf = kelime[-3] if len(kelime) >= 3 else ""
        if onceki_harf in ["a", "ı", "o", "u"]:
            ek = 'dan'
        elif onceki_harf in ["e", "i", "ö", "ü"]:
            ek = 'den'
    elif harfler == 'z':
        onceki_harf = kelime[-2]
        if onceki_harf in ["a", "ı", "o", "u"]:
            ek = 'dan'
        elif onceki_harf in ["e", "i", "ö", "ü"]:
            ek = 'den'
    elif harfler == 's':
        if son_harf in ["a", "ı", "o", "u"]:
            ek = 'dan'
        elif son_harf in ["e", "i", "ö", "ü"]:
            ek = 'den'

    return f"{kelime}'{ek}"

def ninhalii(kelime):
    kelime = kelime.lower()
    harfler = ""
    ek = ""
    son_harf = kelime[-1]
    son_iki_harf = kelime[-2] if len(kelime) >= 2 else ""

   

    if son_harf in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "s"
    elif son_iki_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"] and son_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "zz"
    else:
        harfler = "z"

    if harfler == 'zz':
        onceki_harf = kelime[-3] if len(kelime) >= 3 else ""
        if onceki_harf in ["a", "ı"]:
            ek = 'ın'
        elif onceki_harf in ["e", "i"]:
            ek = 'in'
        elif onceki_harf in ["o", "u"]:
            ek = 'un'
        elif onceki_harf in ["ö", "ü"]:
            ek = 'ün'
    elif harfler == 'z':
        onceki_harf = kelime[-2]
        if onceki_harf in ["a", "ı"]:
            ek = 'ın'
        elif onceki_harf in ["e", "i"]:
            ek = 'in'
        elif onceki_harf in ["o", "u"]:
            ek = 'un'
        elif onceki_harf in ["ö", "ü"]:
            ek = 'ün'
    elif harfler == 's':
        if son_harf in ["a", "ı"]:
            ek = 'nın'
        elif son_harf in ["e", "i"]:
            ek = 'nin'
        elif son_harf in ["o", "u"]:
            ek = 'nun'
        elif son_harf in ["ö", "ü"]:
            ek = 'nün'

    return f"{kelime}'{ek}"

def debhalii(kelime): #de-da bağlacı
    kelime = kelime.lower()
    harfler = ""
    ek = ""
    son_harf = kelime[-1]
    son_iki_harf = kelime[-2] if len(kelime) >= 2 else ""

    print(f"{son_harf}\n")

    if son_harf in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "s"
    elif son_iki_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"] and son_harf not in ["a", "ı", "e", "i", "o", "u", "ö", "ü"]:
        harfler = "zz"
    else:
        harfler = "z"

    if harfler == 'zz':
        onceki_harf = kelime[-3] if len(kelime) >= 3 else ""
        if onceki_harf in ["a", "ı", "o", "u"]:
            ek = 'da'
        elif onceki_harf in ["e", "i", "ö", "ü"]:
            ek = 'de'
    elif harfler == 'z':
        onceki_harf = kelime[-2]
        if onceki_harf in ["a", "ı", "o", "u"]:
            ek = 'da'
        elif onceki_harf in ["e", "i", "ö", "ü"]:
            ek = 'de'
    elif harfler == 's':
        if son_harf in ["a", "ı", "o", "u"]:
            ek = 'da'
        elif son_harf in ["e", "i", "ö", "ü"]:
            ek = 'de'

    return f"{kelime} {ek}"



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
    tarih = date.today().strftime("%Y-%m-%d")
    hikaye_numaralari = hikayeler.split(',')
    hikaye_isimleri = ["hikaye-" + num for num in hikaye_numaralari]

    hikayalar_dizini = os.path.join("hikayeler", cinsiyet, tip)

    for hikaye_adi in hikaye_isimleri:
        original_path = os.path.join(hikayalar_dizini, hikaye_adi + ".docx")
        copy_path = os.path.join(hikayalar_dizini, hikaye_adi + "_" + ad + ".docx")
        shutil.copyfile(original_path, copy_path)

        ihali = ihalii(ad)
        ehali = ehalii(ad)
        dehali = dehalii(ad)
        denhali = denhalii(ad)
        debhali = debhalii(ad)
        ninhali = ninhalii(ad)
        word_replacements = [
            ("Yavuz'u", ihali),
            ("Yavuz'a", ehali),
            ("Yavuz'da", dehali),
            ("Yavuz'dan", denhali),
            ("Yavuz da", debhali),
            ("Yavuz'un", ninhali),
            ("Yavuz", ad),
        ]

        doc = Document(os.path.join(hikayalar_dizini, hikaye_adi + "_" + ad + ".docx"))

        for paragraph in doc.paragraphs:
            for search_word, replace_word in word_replacements:
                if search_word in paragraph.text:
                    for run in paragraph.runs:
                        run.text = run.text.replace(search_word, replace_word)

        doc.save(os.path.join("üretim", ad + "_" + hikaye_adi +"_"+tarih+ ".docx"))
        result_label.config(text="Belgeler başarıyla üretildi!")
        # Orijinal dosyanın kopyasını sil
        os.remove(os.path.join(hikayalar_dizini, hikaye_adi + "_" + ad + ".docx"))
        # Sipariş dosyasını taşı ve adını değiştir
    #txt dosyasını taşı
    # yeni_ad = ad+"-" + tarih + ".txt"
    # shutil.move("siparis.txt", os.path.join("üretilmişler", yeni_ad))

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
