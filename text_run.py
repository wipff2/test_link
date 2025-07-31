import time
import sys

def running_text(text, speed):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print("\n")  # Baris baru setelah selesai satu bagian

# Hitung mundur sebelum mulai
def countdown(start=1, end=3, delay=1.0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(delay)
    print()  # Tambahkan baris kosong sebelum teks utama

# Daftar teks (teks, kecepatan_ketik_per_char, delay_setelah_baris)
lyrics = [
    ("Salahkah bila aku mencintaimu...", 0.05, 2.2),
    ("Dan berharap engkau kan jadi milikku...", 0.04, 2.2),
    ("Walau banyak yang bilang kau tak pantas untukku....", 0.06, 4.9),

    ("Sayang ku mohon jangan tolak cintaku..", 0.05, 2.2),
    ("Jiwa ragaku ini hanya untukkmu..", 0.04, 2.2),
    ("Aku rela berkorban demi cintamu itu....", 0.06, 6.0),

    ("Biarlah orang berkata apa...", 0.05, 5.7),
    ("Manusia tiada yang sempurna...", 0.04, 6.5),
    ("Ku terima kau apa adanya...", 0.05, 5.9),
    ("Yang penting aku bahagia...", 0.03, 5.2),
    ("thanks for watching..", 0.03, 4.2)
]

# Mulai hitung mundur
countdown()

# Jalankan teks berjalan
for line, type_speed, line_delay in lyrics:
    running_text(line, type_speed)
    time.sleep(line_delay)

input("Tekan Enter untuk keluar...")
