from docx import Document

# Word belgesini aç
doc = Document("aaa.docx")

  
search_word = "xxixx"
replace_word = "YeniKelime"

# Tüm paragrafları kontrol et ve değiştir
for paragraph in doc.paragraphs:
    if search_word in paragraph.text:
        for run in paragraph.runs:
            run.text = run.text.replace(search_word, replace_word)

# Değişiklikleri kaydet
doc.save("YeniBelge.docx")
