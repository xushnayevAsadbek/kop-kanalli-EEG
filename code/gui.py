# EEG tahlil dasturi uchun GUI (Grafik Foydalanuvchi Interfeysi) yaratish
import tkinter as tk
from tkinter import filedialog, messagebox
import mne
import matplotlib.pyplot as plt

# Funksiya: EEG faylini tanlash
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("EDF files", "*.edf")])
    file_path_entry.delete(0, tk.END)  # Fayl nomini oynadan tozalash
    file_path_entry.insert(0, filename)  # Tanlangan faylni oynaga kiritish

# Funksiya: EEG faylini yuklab, tahlil qilish
def analyze_data():
    # Faylni yuklash
    file_path = file_path_entry.get()
    
    if file_path:
        try:
            raw = mne.io.read_raw_edf(file_path, preload=True)
            
            # EEG signalni ko'rsatish
            raw.plot(title='EEG signal')

            # Chastota spektral zichligini (PSD) chiqarish
            raw.plot_psd(area_mode='range', tmax=10.0, show=True)

            # Rereferencing
            raw.set_eeg_reference('average')

            # Natijani ko'rsatish
            plt.show()  # Grafikni interaktiv tarzda ko'rsatish
        except Exception as e:
            messagebox.showerror("Xato", f"Faylni yuklashda xato: {e}")
    else:
        messagebox.showwarning("Ogohlantirish", "Fayl tanlanmadi.")

# Tkinter oyna yaratish
root = tk.Tk()
root.title("EEG Tahlil Dasturi")
root.geometry("600x400")  # Oyna o'lchamini belgilash
root.configure(bg="#f0f0f0")  # Oyna fon rangini o'zgartirish

# Tugmalarni joylashtirish uchun ramka
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(expand=True)  # Ramkani markazga joylashtirish

# Faylni tanlash uchun tugma
browse_button = tk.Button(button_frame, text="Faylni tanlash", command=browse_file, bg="#4CAF50", fg="white", font=("Arial", 10), width=20)
browse_button.pack(pady=10)  # Tugma o'rtasida bo'sh joy

# Fayl yo'lini ko'rsatish uchun Entry vidjeti
file_path_entry = tk.Entry(root, width=40, font=("Arial", 12))
file_path_entry.pack(pady=10)

# Tahlil qilish tugmasi
analyze_button = tk.Button(button_frame, text="Yuklash va tahlil qilish", command=analyze_data, bg="#2196F3", fg="white", font=("Arial", 10), width=20)
analyze_button.pack(pady=10)  # Tugma o'rtasida bo'sh joy

# GUI oynasini ishga tushurish
root.mainloop() 
