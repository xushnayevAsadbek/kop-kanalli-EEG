import mne
import matplotlib.pyplot as plt

# EEG faylini yuklash
def load_eeg_data(file_path):
    raw = mne.io.read_raw_edf(file_path, preload=True)
    return raw

# Filtrlanishi (1-40 Hz oraliqda)
def filter_data(raw):
    raw.filter(1., 40., fir_design='firwin')
    return raw

# Referensni sozlash
def set_reference(raw):
    raw.set_eeg_reference('average')
    return raw

# PSD ko'rsatish
def plot_psd(raw):
    raw.plot_psd(area_mode='range', tmax=10.0, show=True)

# EEG ma'lumotlarini vizualizatsiya qilish
def plot_data(raw):
    raw.plot(title="EEG Signal")
