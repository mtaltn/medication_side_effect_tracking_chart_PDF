from fpdf import FPDF

# Yan etki takip çizelgesi verileri
columns = [
    "Gun", "Tarih", "Bulanti / Kusma", "Bas Agrisi", "Karin Agrisi / Kramp",
    "Gogus Hassasiyeti", "Adet Duzensizligi", "Diger Belirtiler", "Notlar"
]


# Günlük satırlar (7 günlük)
rows = [["{}".format(i)] + [""] * (len(columns) - 1) for i in range(1, 8)]

# PDF oluşturma
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=10)

# Başlık
pdf.set_font("Arial", style='B', size=12)
# problemli olanlar: ı → i, ş → s, ğ → g, ü → u, ç → c, ö → o
# örnek başlık satırını şu şekilde düzelt:

pdf = FPDF(orientation='L')  # Yatay modda sayfa oluştur
pdf.add_page()
pdf.set_font("Arial", size=10)

pdf.cell(0, 10, txt="Ilac Yan Etki Takip Cizelgesi (7 Gunluk)", ln=True, align="C")
pdf.ln(5)

# Tablo başlığı
pdf.set_font("Arial", style='B', size=10)
col_widths = [10, 25, 30, 25, 40, 35, 35, 35, 40]
for col_name, width in zip(columns, col_widths):
    pdf.cell(width, 10, col_name, border=1)
pdf.ln()

# Satırları yaz
pdf.set_font("Arial", size=10)
for row in rows:
    for item, width in zip(row, col_widths):
        pdf.cell(width, 10, item, border=1)
    pdf.ln()

# PDF dosyasını kaydet
pdf.output("Ilac_Yan_Etki_Takip_Cizelgesi.pdf")
