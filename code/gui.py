
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
root.geometry("400x200")  # Oyna o'lchamini belgilash
root.configure(bg="#f0f0f0")  # Oyna fon rangini o'zgartirish

# Faylni tanlash uchun tugma
browse_button = tk.Button(root, text="Faylni tanlash", command=browse_file, bg="#4CAF50", fg="white", font=("Arial", 12))
browse_button.pack(pady=10, padx=20, fill='x')  # Tugma o'rtasida bo'sh joy va kengaytirish

# Fayl yo'lini ko'rsatish uchun Entry vidjeti
file_path_entry = tk.Entry(root, width=50, font=("Arial", 12))
file_path_entry.pack(pady=10)

# Tahlil qilish tugmasi
analyze_button = tk.Button(root, text="Yuklash va tahlil qilish", command=analyze_data, bg="#2196F3", fg="white", font=("Arial", 12))
analyze_button.pack(pady=10, padx=20, fill='x')  # Tugma o'rtasida bo'sh joy va kengaytirish

# GUI oynasini ishga tushurish
root.mainloop()

# ----------======



# import tkinter as tk
# from tkinter import filedialog
# from eeg_processing import load_eeg_data, filter_data, set_reference, plot_psd, plot_data

# # GUI oynasini yaratish
# def create_gui():
#     window = tk.Tk()
#     window.title("EEG Data Analysis")
#     window.geometry("400x300")

#     # Yuklash tugmasi
#     def load_file():
#         file_path = filedialog.askopenfilename(filetypes=[("EDF files", "*.edf")])
#         raw = load_eeg_data(file_path)
#         raw = filter_data(raw)
#         raw = set_reference(raw)
#         plot_data(raw)
#         plot_psd(raw)
        
#     load_button = tk.Button(window, text="Yuklash va Tahlil qilish", command=load_file)
#     load_button.pack(pady=20)
    
#     window.mainloop()

# # GUI ishga tushurish
# if __name__ == "__main__":
#     create_gui()


# import tkinter as tk
# from tkinter import filedialog
# import mne
# import matplotlib.pyplot as plt

# # Funksiya: EEG faylini tanlash
# def browse_file():
#     filename = filedialog.askopenfilename(filetypes=[("EDF files", "*.edf")])
#     file_path_entry.delete(0, tk.END)  # Fayl nomini oynadan tozalash
#     file_path_entry.insert(0, filename)  # Tanlangan faylni oynaga kiritish

# # Funksiya: EEG faylini yuklab, tahlil qilish
# def analyze_data():
#     # Faylni yuklash
#     file_path = file_path_entry.get()
    
#     if file_path:
#         raw = mne.io.read_raw_edf(file_path, preload=True)
        
#         # EEG signalni ko'rsatish
#         raw.plot(title='EEG signal')

#         # Chastota spektral zichligini (PSD) chiqarish
#         raw.plot_psd(area_mode='range', tmax=10.0, show=True)

#         # Rereferencing
#         raw.set_eeg_reference('average')

#         # Natijani ko'rsatish
#         plt.show()  # Grafikni interaktiv tarzda ko'rsatish
#     else:
#         print("Fayl tanlanmadi.")

# # Tkinter oyna yaratish
# root = tk.Tk()
# root.title("EEG Tahlil Dasturi")

# # Faylni tanlash uchun tugma
# browse_button = tk.Button(root, text="Faylni tanlash", command=browse_file)
# browse_button.pack()



# # Fayl yo'lini ko'rsatish uchun Entry vidjeti
# file_path_entry = tk.Entry(root, width=50)
# file_path_entry.pack()

# # Tahlil qilish tugmasi
# analyze_button = tk.Button(root, text="Yuklash va tahlil qilish", command=analyze_data)
# analyze_button.pack()

# # GUI oynasini ishga tushurish
# root.mainloop()

