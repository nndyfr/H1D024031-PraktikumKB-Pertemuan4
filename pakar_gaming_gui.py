import tkinter as tk
from tkinter import messagebox

# Data Kerusakan & Gejala
database_kerusakan = {
    "VGA Overheat": ["fps_drop", "laptop_panas", "kipas_berisik"],
    "RAM Kurang": ["game_lag", "stuttering", "loading_lama"],
    "Driver VGA Bermasalah": ["game_crash", "layar_blank", "artefak"],
    "CPU Bottleneck": ["fps_drop", "cpu_100", "game_tidak_stabil"],
    "Storage Lambat": ["loading_lama", "texture_lambat", "game_stuck"]
}

solusi_kerusakan = {
    "VGA Overheat": "Bersihkan kipas dan gunakan cooling pad",
    "RAM Kurang": "Upgrade RAM minimal 8GB atau 16GB",
    "Driver VGA Bermasalah": "Update atau install ulang driver VGA",
    "CPU Bottleneck": "Turunkan setting game atau upgrade CPU",
    "Storage Lambat": "Gunakan SSD untuk performa lebih cepat"
}

# Daftar Gejala
semua_gejala = [
    ("fps_drop", "Apakah game mengalami FPS drop?"),
    ("laptop_panas", "Apakah laptop terasa sangat panas saat bermain?"),
    ("kipas_berisik", "Apakah kipas berbunyi keras?"),
    ("game_lag", "Apakah game terasa lag?"),
    ("stuttering", "Apakah game tersendat-sendat (stuttering)?"),
    ("loading_lama", "Apakah loading game lama?"),
    ("game_crash", "Apakah game sering crash/keluar sendiri?"),
    ("layar_blank", "Apakah layar tiba-tiba blank saat bermain?"),
    ("artefak", "Apakah muncul garis atau glitch di layar?"),
    ("cpu_100", "Apakah penggunaan CPU selalu 100%?"),
    ("game_tidak_stabil", "Apakah performa game tidak stabil?"),
    ("texture_lambat", "Apakah tekstur game muncul terlambat?"),
    ("game_stuck", "Apakah game sering stuck/freeze?")
]

# Class Aplikasi
class SistemPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Gaming Laptop")
        self.root.geometry("450x300")

        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # Label
        self.label_tanya = tk.Label(root, text="Selamat Datang di Sistem Pakar", font=("Arial", 12))
        self.label_tanya.pack(pady=20)

        # Tombol mulai
        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai)
        self.btn_mulai.pack(pady=10)

        # Frame jawaban
        self.frame_jawab = tk.Frame(root)

        self.btn_ya = tk.Button(self.frame_jawab, text="YA", width=10, command=lambda: self.jawab("y"))
        self.btn_tidak = tk.Button(self.frame_jawab, text="TIDAK", width=10, command=lambda: self.jawab("t"))

        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    # Mulai
    def mulai(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.btn_mulai.pack_forget()
        self.frame_jawab.pack(pady=20)

        self.tampilkan_pertanyaan()

    # Tampilkan Pertanyaan
    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    # Jawaban User
    def jawab(self, respon):
        if respon == "y":
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    # Proses Hasil
    def proses_hasil(self):
        skor_tertinggi = -1
        hasil = ""
        solusi = ""

        for kerusakan, gejala in database_kerusakan.items():
            skor = 0
            for g in gejala:
                if g in self.gejala_terpilih:
                    skor += 1

            if skor > skor_tertinggi:
                skor_tertinggi = skor
                hasil = kerusakan
                solusi = solusi_kerusakan[kerusakan]

        # Hitung persentase keyakinan
        total_gejala = len(database_kerusakan[hasil])
        persentase = (skor_tertinggi / total_gejala) * 100

        messagebox.showinfo(
            "Hasil Diagnosa",
            f"Kerusakan yang paling mungkin:\n\n{hasil}"
            f"\n\nTingkat keyakinan: {persentase:.0f}%"
            f"\n\nSolusi:\n{solusi}"
        )

        # Reset
        self.frame_jawab.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa selesai. Ingin mencoba lagi?")

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemPakar(root)
    root.mainloop()