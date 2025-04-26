
import mne
from eeg_processing import load_eeg_data, filter_data, set_reference
from eeg_visualization import save_psd_and_raw_plots  # To'g'ri import

# EEG faylini yuklash
raw = load_eeg_data("D:\\EEG\\data\\subject04.edf")

# Filtrlash
raw = filter_data(raw)

# Referens sozlash
raw = set_reference(raw)

# PSD va Raw signal grafikalarini saqlash
save_psd_and_raw_plots(raw)
