from docx import Document
import os
import shutil

# Verileri al
ad = "salih"
hikayeler = "1,2,3"
cinsiyet = "erkek"
tip = "karma"

# Hikayeleri ayır ve hikaye isimlerini oluştur
hikaye_numaralari = hikayeler.split(',')
hikaye_isimleri = ["hikaye-" + num for num in hikaye_numaralari]

# Hikayeler dizini oluştur
hikayalar_dizini = os.path.join("hikayeler", cinsiyet, tip)

# Orijinal dosyaların kopyalarını oluştur
for hikaye_adi in hikaye_isimleri:
    original_path = os.path.join(hikayalar_dizini, hikaye_adi + ".docx")
    copy_path = os.path.join(hikayalar_dizini, hikaye_adi + "_" + ad  + ".docx")
    shutil.copyfile(original_path, copy_path)

# Her hikaye için işlem yap
for hikaye_adi in hikaye_isimleri:
    # Kopya Word belgesini aç
    doc = Document(os.path.join(hikayalar_dizini, hikaye_adi + "_" + ad  + ".docx"))
    
    search_word = "Xxixx"
    replace_word = ad  # Yeni ismi oluştur

    # Tüm paragrafları kontrol et ve değiştir
    for paragraph in doc.paragraphs:
        if search_word in paragraph.text:
            for run in paragraph.runs:
                run.text = run.text.replace(search_word, replace_word)

    # Değişiklikleri kaydet
    doc.save(os.path.join(hikaye_adi + "_" + ad  + ".docx"))
