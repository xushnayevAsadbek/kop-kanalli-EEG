import mne
import matplotlib.pyplot as plt

# 1. EEG faylini yuklash (masalan, .edf fayl)
# Fayl yo'lini to'g'ri ko'rsatganingizga ishonch hosil qiling
raw = mne.io.read_raw_edf('subject03.edf', preload=True)

# 2. Filtrlash (1-40 Hz oraliqda)
raw.filter(1., 40., fir_design='firwin')

# 3. EEG signalini ko'rsatish
raw.plot(title='Asl EEG signal')

# 4. PSD (chastotaviy spektral zichlik) ko'rsatish
raw.plot_psd(area_mode='range', tmax=10.0, show=True)

# 5. Voqealarni aniqlash va ERP olish
# Eslatma: sample_data.edf faylda voqealar bo'lishi kerak
# Bu kod test maqsadida
# events = mne.find_events(raw)
# epochs = mne.Epochs(raw, events, event_id={'stimulus': 1}, tmin=-0.2, tmax=0.5)
# evoked = epochs.average()
# evoked.plot()
