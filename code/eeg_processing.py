import mne
import os
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

# Grafikalarni saqlash
def save_psd_and_raw_plots(raw):
    # Fayl papkalarini yaratish
    if not os.path.exists('results/psd_plots'):
        os.makedirs('results/psd_plots')

    if not os.path.exists('results/raw_plots'):
        os.makedirs('results/raw_plots')

    # PSD grafikasini saqlash
    fig_psd = raw.plot_psd(area_mode='range', tmax=10.0, show=False)
    fig_psd.savefig('results/psd_plots/psd_signal_1.png')

    # Raw signal grafikasi saqlash
    fig_raw = raw.plot(title="EEG Signal", show=False)
    fig_raw.savefig('results/raw_plots/raw_signal_1.png')

if __name__ == "__main__":
    # Faylni yuklash
    raw = load_eeg_data("data/subject03.edf")   # <- Bu senga kerakli edf fayl

    # Filtr
    raw = filter_data(raw)

    # Referens
    raw = set_reference(raw)

    # PSD grafigini chizish
    plot_psd(raw)

    # EEG signalini chizish
    plot_data(raw)

    # Grafikalarni saqlash
    save_psd_and_raw_plots(raw)
